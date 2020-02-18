Mindmap project

Prerequsites:
   - Docker

<h1>To run</h1>
<br>In the root directory of this project run:</br>
  <br>docker build -t mindmap:latest .</br>
  <br>docker run -d -p 5000:5000 mindmap:latest</br>
<br>This will run the Api on your local machine via port 5000.</br>
<br>Point tests to http://localhost:5000</br>

<h1>Please Note</h1>
<br>There are still many items to finish on this project such as:</br>
<li>Using Messages in Unit Test Assertions</li>
<li>Adding more integration tests for read leaf</li>
<li>Creating a Models Directory</li>
<li>Splitting up app.py</li>
