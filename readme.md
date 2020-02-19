Mindmap project

Prerequsites:
   - Docker

<h1>To run</h1>
<h2>Option 1 - Pull From DockerHub</h2>
<code>docker pull thomasrice1234/mindmap:latest</code>
<br></br>
<code>docker run -d -p 5000:5000 thomasrice1234/mindmap:latest</code>

<h2>Option 2 - Build & Run Dockerfile</h2>
<br>In the root directory of this project run:</br>
  <code>docker build -t mindmap:latest .</code>
  <br></br>
  <code>docker run -d -p 5000:5000 mindmap:latest</code>
<br>This will run the Api on your local machine via port 5000.</br>
<br>Point tests to http://localhost:5000</br>

<h1>Please Note</h1>
<br> All data added is bound to the lifetime of the container as it uses a sqlite file - use the -v option of Docker run to map the sqlite file to your local system</br>
<br>There are still many items to finish on this project such as:</br>
<li>Using Messages in Unit Test Assertions</li>
<li>Adding more integration tests for read leaf</li>
<li>Creating a Models Directory</li>
<li>Splitting up app.py</li>
