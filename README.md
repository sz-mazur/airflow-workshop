# airflow-workshop

## Repository information

| Property      |                                    Value                                    |
|---------------|:---------------------------------------------------------------------------:|
| Owner         |                                 Alan Głodek                                 |
| Documentation | [wiki](https://wiki.datumo.io/new_joiners/repozytoria_szkoleniowe/airflow)  |
| Useful links  |                         [See section](#used-tools)                          |

---
## Overview
This workshop is dedicated for person who has basic knowledge of Docker and Python.
Also, you don't need to have any experience in the Airflow.
The aim of the course is initiation into Airflow and set path for the better understanding scheduling.

## Project structure
```
├── airflow_local
├── config
├── tasks
│   └── task1
│   └── ...
├── tests
│   └── task0
│   └── ...
```

## Prerequisites
The basic knowledge of:
* Python
* Docker

## Before you begin
Please, make sure that you have set up correctly **Python** and **Docker** (including Docker Compose).

### Python
This workshop was founded upon:
* [Python](https://www.python.org/) 3.11
* [Pipenv](https://pipenv.pypa.io/en/latest/) 2022.12.19

To check that you have everything what you need, run command below:
```
python --version
pipenv --version
```
**Note:** if `python --version` doesn't work try to use `python3 --version` insted.

The output should look like:
```
Python 3.11.0rc1
pipenv, version 2022.12.19
```
**IMPORTANT**: If you have an error during this command or different version, go to the [Used tools](#used-tools) and see how to install Python/Pipenv.

Another requirements will be installed from Pipenv dependency. You can find it in [Pipfile](Pipfile).

To install dependency in your project, run:
```
pipenv install
```
**IMPORTANT**: In this project we give you generated [Pipfile.lock](Pipfile.lock) file,
which means you don't need to execute `pipenv lock` command.
But if your PyCharm may have problem with it just regenerate this file:
1. deleting existing [Pipfile.lock](Pipfile.lock)
2. run `pipenv update`

### Docker
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/) v1.29.1 or newer

To double-check that everything is fine, type in console:
```
docker --version
docker compose version
```
The output should look like:
```
Docker version 20.10.21, build baeda1f
Docker Compose version v2.13.0
```
**IMPORTANT**: If you have an error during this command or different version go to the [Used tools](#used-tools) and see how to install Docker.

**TIP:**
The default amount of memory available for Docker on macOS is often not enough to get up and run Airflow.
If enough memory is not allocated, it might lead to the webserver continuously restarting.
You should allocate at least 4GB memory for the Docker Engine (**ideally 8GB**).

You can make sure if you have enough memory by running this command:
```
sudo docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
```

---
## `airflow_control.sh` script
For ease of use, a bash script named `airflow_control.sh` has been written. It contains all the commands listed below for managing the Airflow cluster on Docker.
This script allows for quick initialization of the Airflow cluster, its start, stop, and cleanup (see cleanup section).
Run this script in terminal with following command:

````
bash airflow_control.sh <one of commands below>
````

| Command  | Description                                                                    |
|----------|--------------------------------------------------------------------------------|
| init     | Create required directories and .env file, running docker compose init.        |
| up       | Runs docker compose up so you can start working on airflow service.            |
| down     | Runs docker compose down after you stop working on airflow service.            |
| cleanup  | Returns to the state from before setup. Removes images, volumes, working dirs. |
| help     | Show help message.                                                             |


---
## Task 0 - Prepare environment
Glad to see you here! Let's quickly prepare your environment!

To do this, firstly create cluster Airflow on Docker.

**Hint**: Whole process described below can be done with running ``bash airflow_control.sh init``.

Deploy Airflow on Docker Compose using `docker-compose.yaml` file from the [airflow_local](airflow_local) folder.
If you need more information about docker-compose file see [used tools section](#used-tools).

Before starting Airflow for the first time, you need to prepare your environment, i.e. create the necessary files, directories and initialize the database.
On Linux, the quick-start needs to know your host user id and needs to have group id set to 0.
Otherwise, the files created in dags, logs and plugins will be created with root user ownership.
You have to make sure to configure them for the docker-compose,
so open `airflow_local` folder in terminal then run these commands:
````
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
````
**Why are we creating these folders?**

Some directories in the container are mounted, which means that their contents are synchronized between your computer and the container.

* **./dags** - you can put your DAG files here.
* **./logs** - contains logs from task execution and scheduler.
* **./plugins** - you can put your custom plugins here.

After creating these folders it's time to initialize the database.
On all operating systems, you need to run database migrations and create the first user account. To do this, run:
```
sudo docker compose up airflow-init
```
After initialization is complete, you should see a message like this:
```
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.5.0
start_airflow-init_1 exited with code 0
```
**Hint**: In some cases you may have permission warning related to Airflow 3.0, but no worries, we use 2.5 version.

Perfect! It's time to run Airflow!
```
sudo docker compose up
```
To see that everything is alright, you can check the condition of the containers and make sure that no containers are in an unhealthy condition:
```
sudo docker ps
```
The output should look like:
```
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
3d272f55aecd   apache/airflow:2.5.0   "/usr/bin/dumb-init …"   20 minutes ago   Up 20 minutes (healthy)   8080/tcp                                    airflow_local-airflow-scheduler-1
0efcfcc691f6   apache/airflow:2.5.0   "/usr/bin/dumb-init …"   20 minutes ago   Up 20 minutes (healthy)   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   airflow_local-airflow-webserver-1
cd71e91679de   apache/airflow:2.5.0   "/usr/bin/dumb-init …"   20 minutes ago   Up 20 minutes (healthy)   8080/tcp                                    airflow_local-airflow-worker-1
1483917a47ba   apache/airflow:2.5.0   "/usr/bin/dumb-init …"   20 minutes ago   Up 20 minutes (healthy)   8080/tcp                                    airflow_local-airflow-triggerer-1
4a61e5ebc141   postgres:13            "docker-entrypoint.s…"   30 minutes ago   Up 30 minutes (healthy)   5432/tcp                                    airflow_local-postgres-1
b0567c43a132   redis:latest           "docker-entrypoint.s…"   30 minutes ago   Up 30 minutes (healthy)   6379/tcp                                    airflow_local-redis-1
```

It's time to go to the web interface!
The webserver is available at: http://localhost:8080.
The default account has the login **airflow** and the password **airflow**.

To double-check that everything is ok, go to the [task0](tests%2Ftask0) folder and run [test.py](tests%2Ftask0%2Ftest.py).

**Hint:** You can also run test via follow command: `pytest tests/task0/test.py` from project directory.

If everything lights on green you can move forward to [Task 1](#task-1).

---
## Task 1

Firstly, please go to the [example_dag.py](tasks%2Ftask1%2Fexample_dag.py) in `tasks/task1` folder and see construction of DAG.
There is a couple of comments that will help you understand what DAG does.
If you need more information about DAG please see [airflow section](#airflow).

The next step is to copy this example into [dags](airflow_local%2Fdags) folder
and after ~30s you will see the DAG on [UI](http://localhost:8080).
When you put DAG into the folder, in this time Airflow Scheduler is running `DagFileProcessorManager` and checking your new DAG.
You can find more about Airflow File Processing [here](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dagfile-processing.html).

Now it's time to run your first DAG.
To run DAG with additional parameters click `play` symbol then `Trigger DAG w/ config`.

![run-dag-with-param.png](assets%2Fimg%2Frun-dag-with-param.png)

Afterwards, put `name` param in JSON config and click `trigger`. If you get notification on blue background:
`Triggered example_dag, it should start any moment now.` It means that DAG run successfully.
To get more information about states of Task visit: [Task Instances](https://airflow.apache.org/docs/apache-airflow/stable/concepts/tasks.html#task-instances).

It's time for practical test!
In `tasks/task1` folder there is [questions.md](tasks%2Ftask1%2Fquestions.md)
file including a couple of questions. Please answer shortly (max 2-3 sentences for each one).

To go forward, make sure that all tests located at [test.py](tests%2Ftask1%2Ftest.py) are green.

---
## Task 2
Perfect! Now you know how to manage and run DAGs.
It's time to write the first DAG. We will build it in four steps.
After each step you can run test prepared for it to make sure that everything is ok.
For example, for step 1 you have to run `test_step1.py` from `tests/task2` folder.
To do this task, you may need also data located in `tasks/task2` folder in [sales_native.csv](tasks%2Ftask2%2Fsales_native.csv) file.

**HINT**: To copy needed files to dags directory you can run:
```
python deploy_dags.py 2
```
**HINT**: If you need to create an additional files and import it to the DAG, usefully will be creating file structure like this:
```
- dags/
|- tasks/
| | -  task2/
| | | - task2_dag.py
| | | - file1.py
| | | - file2.py
```

### Steps description
**Step 1**

Please create and implement on Airflow DAG in file [task2_sales_dag.py](tasks%2Ftask2%2Ftask2_sales_dag.py)
located at `tasks/task2` folder with the following settings:

| param name | value           |
|------------|-----------------|
| id         | task2_sales_dag |
| start_date | 2023.01.01      |
| schedule   | once            |
| tags       | task2           |

Then create 2 [PythonOperators](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html).
The first one should read the data file and calculate mean revenue for each `orderMethodType` and save results to the file as `task2_mean_revenue.csv`.
The second one should calculate the max revenue for each `orderMethodType` and also save to file as `task2_max_revenue.csv`.
For test perspective, please name first operator as `mean_revenue` and the second as `max_revenue`.

**Requirements:**
- keep data files in `dags/data` folder,
- save output files into `dags/output` folder. Please remember to put Docker path of DAGs folder `/opt/airflow/` (not your locally project path).
In this case useful will be using variables from `config/config.py` file,
- to load files use `op_kwargs` by putting absolute path to the file,
- to find mean and max use [Pandas](https://pandas.pydata.org/docs/).

**Step 2**

Perfect, the next steps is creating next PythonOperator.
The goal of this operator is to calculate difference between max revenue and mean for each orderMethodType.
Please, remember that this operator should begin after the previous one (`mean_revenue` and `max_revenue`).
For more information go to [managing dependencies](https://docs.astronomer.io/learn/managing-dependencies).
For testing perspective please name this third operator as `diff_revenue` and save data as `task2_difference_revenue.csv`.

After that, it's time to delete `data/sales_native.csv`.
To do that, please create next PythonOperator that delete this data file. Put the id of these operator to `delete_source_file`.
Make sure that previous tasks end successfully by setting `trigger_rule` to `none_failed`,
see [Trigger rules](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html#trigger-rules).

**Step 3**

Our analysts found bug after step 2. There is possibility to run flow without source file!
Try to prevent that by using [FileSensor](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/sensors/filesystem/index.html#module-airflow.sensors.filesystem).
Call this sensor as `waiting_for_data`.

**HINT**: Remember to create `file connection` with `fs_default` ID. [See more information about connection](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html).

**Step 4**

In this last step we will create [custom Operator](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html#) to print into logs final output of all previous tasks `diff_revenue, max_revenue, mean_revenue`.

**Requirements:**
- name this operator as `workflow_finished_operator`,
- use [Templateable fields](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html#templating) to make sure that operator can take only csv file,
- make sure that this operator will run after `diff_revenue`.


---
## Task 3
In this final task we will learn what exactly [schedule](https://airflow.apache.org/docs/apache-airflow/2.5.0/concepts/scheduler.html#) is and how to schedule DAG's.
As the previous task, for better understanding problem, we will split this task into 3 steps:
1. How to manage schedule in DAG?
2. How to read intervals and manage date time?
3. What impact `max_active_tasks`, `max_active_runs` and `depends_on_past` have on task scheduling?

**HINT**: To copy needed files to dags directory you can run:
```
python deploy_dags.py 3
```

**Step 1**

In these steps we would like to learn what exactly schedule is and how to manage it in Airflow.
Base on DAG `step1_1` located in [task3](tasks%2Ftask3), please:
- change schedule interval to `daily`,
- change start date on `now()`,
- try get `ds` variable from Airflow see [Templates](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) for more information.

Unpause DAG and see what's happened.
In given comment section (inside [step1_1.py](tasks%2Ftask3%2Fstep1_1.py) file) explain what happens and if it works or not + tell why.

Now let's go to the `step1_2` DAG and do the same changes, but change `start_date` to 4 day before
(based on static date, using `date_ago` is bad practice). In given space, tell us what's happened after this small change.
Don't forget to unpause DAG to see difference!

In `step1_3` do the same changes as in previous in `step1_2`, but add additional option to dag `catchup=False`.
[See more information about catchup](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html#catchup).
What happens when we have 4 days ago at `start_date` but `catchup` on false?

**Warning**:
For test perspective, if you want to test `step1_2` or `step1_3`  by `tests/task3/step1_X`
in different day, like you made changes in `start_date`, you must change this date again and redeploy DAG on Airflow.

**Step 2**

It's a quiz time! In this step we prepared for you 3 series of questions.
Each series was located in `tasks/task3/` folder. To check correctness your answers go to `tests/task3/` and run unit test.
To make easier for you, name of the file in `tasks` folder will be the same in the `tests` folder.
For `step2_3` we don't except any unit tests.
Below links to quizes:
 - [step2_1.py](tasks%2Ftask3%2Fstep2_1.py) – quiz about `ds` and `ts` value. If you need more information see [Templates](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html).
 - [step2_2.py](tasks%2Ftask3%2Fstep2_2.py) – quiz about creating crons. See [DAG runs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html).
 - [step2_3.py](tasks%2Ftask3%2Fstep2_3.py) – quiz about macros in Airflow.

**Step 3**

Now we will focus on analysing and simulate long-term processing of DAG.
First lets see what happen in [step3_1.py](tasks%2Ftask3%2Fstep3_1.py) file.
Files [step3_2.py](tasks%2Ftask3%2Fstep3_2.py), [step3_3.py](tasks%2Ftask3%2Fstep3_3.py) are just a copy of this DAG for future tasks to do.

In these steps we'd like to ask you to do three analyses:
1. In the [step3_1.py](tasks%2Ftask3%2Fstep3_1.py) please limit the number of parallel tasks to 2 in one `dag_run`.
2. In the [step3_2.py](tasks%2Ftask3%2Fstep3_2.py) please limit the number of parallel running DAG runs to 2 also include limit from point **1**.
3. In the [step3_3.py](tasks%2Ftask3%2Fstep3_3.py) please do the same things like in point **1** and **2** plus
for the first 5 tasks in the DAG, add a constraint that the task will run only if the corresponding task instance in the previous `dag_run` was successful.

To make sure that you do it correctly, please run the tests from `tests/task3`.

---
## At the end
That's it! If you want to delete Airflow on your host, go to the [Cleaning-up section](#cleaning-up-the-airflow-environment).

**Remember**:
The docker-compose environment that we have prepared is a “quick-start” one.
It was not designed to be used in production, and it has a couple of caveats.

---
## Cleaning-up the Airflow environment

There are two ways you can clean up your local Airflow environment.

1. To reset to the state before Airflow environment setup please run:
    ````
    bash airflow_control.sh cleanup
    ````
2. You can also choose to do it manually.
    1. From `airflow_local` directory, run ``sudo docker compose down --volumes --rmi all`` to shut down Airflow cluster and remove all volumes and images.
    2. Remove ``/dags``, ``/logs`` and ``/plugins`` directories with ``sudo rm -rf dags logs plugins``
    3. Remove the ``.env`` file.
---
## Used tools

- [Airflow](https://airflow.apache.org/) – platform to schedule and monitor workflows
- [Pandas](https://pandas.pydata.org/docs/) – Working with dataframe
- [cron converter](https://pypi.org/project/cron-converter/) – Cron string parser
- [Docker](https://docs.docker.com/) – platform that allows you to build, test, and deploy applications quickly
- [GitHub Actions](https://docs.github.com/en/actions/quickstart) – CI/CD tool
- [PyTest](https://docs.pytest.org/en/7.2.x/) – Testing framework
- [Pipenv](https://pipenv.pypa.io/en/latest/) – Dependency manager
- [pre-commit](https://pre-commit.com) – pre-commit GitHub hooks manager
- [black](https://black.readthedocs.io) – Linter
- [flake8](https://flake8.pycqa.org) – Linter
- [mypy](https://www.mypy-lang.org/) - type checker

## Airflow

- [Concepts](https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html)
- [Architecture Overview](https://airflow.apache.org/docs/apache-airflow/stable/concepts/overview.html#architecture-overview)
- [Best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html)
- [Loading DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html#loading-dags)
- [DAG File Processing](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dagfile-processing.html)
- [Scheduler](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html#scheduler)
- [Operators](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/index.html)
- [Task Instances](https://airflow.apache.org/docs/apache-airflow/stable/concepts/tasks.html#task-instances)
- [Trigger rules](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html#trigger-rules)
- [FileSensor](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/sensors/filesystem/index.html#module-airflow.sensors.filesystem)
- [Connection](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html)
- [Templates reference](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html)
- [Catchup](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html#catchup)

## Docker

- [How to install Docker on linux (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)
- [How to install Docker Desktop on Linux (Ubuntu)](https://docs.docker.com/desktop/install/ubuntu/) – it also including Docker Compose
- [Use Docker Compose](https://docs.docker.com/get-started/08_using_compose/)

## Pipenv

Pipenv helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack
everywhere.  Pipenv uses the [Pipfile](Pipfile) file to orchestrate the project and its dependencies.

### how to install:

To install Pipenv use command bellow:
```
pip install --user pipenv
```

### basic commands:

- `pipenv install` – Install dependencies from `Pipfile` file.
- `pipenv install <package>` – Adds required packages to your `Pipfile` and installs them.
- `pipenv update` - run `pipenv lock` command then install all packages specified in `Pipfile.lock`.
- `pipenv lock` – To pin manually added dependencies from your `Pipfile` file to `Pipfile.lock`.
- `pipenv graph` – Show a active dependency graph of `Pipfile.lock`.
- `pipenv run <command>` – Run command from the virtualenv, e.g. `pipenv run pytest tests/task0_test.py`


## pre-commit

Python package which allows you to create and execute hooks before every commit. All hooks are defined in the `.pre-commit-config.yaml` file.

### quick start:

- `pre-commit install` to initialize the git hooks.
- `pre-commit run --all-files` runs all hooks manually.
