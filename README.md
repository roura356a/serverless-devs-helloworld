<h1>Serverless Devs "Hello World"</h1>
<h2>Installing Serverless Devs</h2>
Once we have the above project structure ready, follow the next steps:
<ul>
 	<li><a href="https://nodejs.org/en/download/">Install <strong>Node.js</strong></a> (<em>&gt;=10.8.0</em>) and <strong>NPM</strong> package management tools</li>
 	<li>Install <strong>Serverless Devs</strong> by running <code>npm install @serverless-devs/s -g</code></li>
 	<li>Check if Serverless Devs is working properly by running <code>s -v</code></li>
</ul>
After installing, you should run <code>s config add</code> to start the setup, choose "Alibaba Cloud (alibaba)" and follow the instructions to put your Alibaba Cloud credentials.

&nbsp;
<h2>Deployment</h2>
Once we have everything ready, let's rock. This, as the last step, is the easiest of all of them, we just need to run <code>s deploy</code> and focus on the output, as we will have all the information we need in order to test if our code is running successfully.

&nbsp;

Thank you for reading all the way to this point, enjoy serverlessing!
