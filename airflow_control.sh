#!/bin/bash

# Help message
show_help() {
    echo "Usage: $0 <command>"
    echo "This script is intended to control your local airflow infrastructure."
    echo "Commands:"
    echo "  init         Create required directories and .env file."
    echo "  up           Runs docker compose up so you can start working on airflow service."
    echo "  down         Runs docker compose down after you stop working on airflow service."
    echo "  cleanup      Returns to the state from before setup. Removes images, volumes, working dirs."
    echo "  help         Show this help message."
}

remove_directories() {
    for dir in "$@"; do
        if [ -d "$dir" ]; then
            echo "Removing directory: $dir"
            rm -r "$dir"
        else
            echo "Directory does not exist: $dir"
        fi
    done
}

remove_env_file() {
    if [ -f ".env" ]; then
      rm ".env"
      echo "Removed .env file"
    else
      echo ".env file does not exist"
    fi
}

create_airflow_folders() {
    if [ ! -d "dags" ]; then
        mkdir dags
        echo "Created dags folder."
    else
        echo "dags folder already exists."
    fi

    if [ ! -d "logs" ]; then
        mkdir logs
        echo "Created logs folder."
    else
        echo "logs folder already exists."
    fi

    if [ ! -d "plugins" ]; then
        mkdir plugins
        echo "Created plugins folder."
    else
        echo "plugins folder already exists."
    fi
}

create_env_file() {
  echo -e "AIRFLOW_UID=$(id -u)" > .env
}

init() {
  echo "Initializing airflow setup..."
  create_airflow_folders
  create_env_file
  sudo docker compose up airflow-init
}

up() {
  if [ -f ".env" ]; then
    echo "Started airflow with docker-compose..."
    sudo docker compose up
  else
    echo "There is no .env file created. Make sure Airflow is set up correctly, by running this script with init param."
  fi
}

down() {
  echo "Shut down airflow service..."
  sudo docker compose down
}

cleanup() {
  echo "Started resetting to pre-setup state..."
  sudo docker compose down --volumes --rmi all
  directories=("dags" "logs" "plugins")
  remove_directories "${directories[@]}"
  remove_env_file
  echo "Removed .env file"
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
    exit 0
fi

if [ $# -ne 1 ]; then
    echo "Error: Incorrect number of arguments."
    show_help
    exit 1
fi

command=$1

cd airflow_local

case "$command" in
    "init")
        init
        echo "Initialization completed!"
        ;;
    "up")
        up
        echo "Setting up Airflow cluster is completed!"
        ;;
    "down")
        down
        echo "Shutting down Airflow cluster is completed!"
        ;;
    "cleanup")
        cleanup
        echo "Cleaning up process is completed!"
        ;;
    *)
        echo "Error: Unknown command: $command"
        show_help
        cd ..
        exit 1
        ;;
esac
cd ..
