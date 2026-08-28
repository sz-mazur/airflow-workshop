## Questions to task 1

Please answer shortly (max 2-3 sentences for each one) to the following questions:

### How to check output of `hello` and `try_number` tasks?
**Answer:**
We can check the Logs of a specific Task by selecting its instance in the **Grid** tab of the DAG, 
then opening the **Logs**.

### How to generate situation when `try_number` returns more than `1`?
**Answer:**
The first try should fail, and **retries** should be set to more than 1, 
so when the said fail happens - airflow does the retry and counter **try_number** goes up.

### How to clear only failed task instances in `hello` task?
**Answer:**
In the Graph tab select `hello` task, then in the Task Actions section there is a **Clear** Action button - 
select **Failed** next to the Clear, then click the Clear button.
