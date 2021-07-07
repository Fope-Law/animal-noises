# Animal Noises Task

Your task is to make a basic microservice app that gets **animals** and their related **noises** from a separate API. Every time the user refreshes, the page should display the **animal** and **noise** in the format: `The pig goes oink`, `The cow goes moo`, `The horse goes neigh`.

The server and API must be *containerised*.

This repo serves as a template for this task. You simply need to fork and clone it to your VMs to get started.

There are some constraints:
- The **animal** must be retrieved using a `GET` request to the API from the server.
- The **noise** must be retrieved using a `POST` request to the API from the server.
- The **noise** *must* be related to the type of **animal**, i.e. the pig cannot go moo.

Write unit tests for both services.

**Stretch Goals:**
- Persist your **animals** and their **noises** to a database, such that the web page can show the last 5 animals with their noises. You may use a MySQL container or a GCP SQL instance.
- Separate the **animal** and **noise** generation functions into two separate APIs