<html>
<head>
  <title>Greetings</title>
</head>
<body>
	<form name="test" method="GET" action="/main/index">
	Twitter Username: <input type="text" name="uname" />
	               <input type="submit" name="submit" value="Submit" />
	</form>
	<hr />
  <h1>${c.user} likes these:</h1>
  <table>
  %for item in c.favs:
    <tr><td><a href="http://twitter.com/${item.author}">${item.author}<a></td><td><% context.write(item.tweet) %>
    <a href="${item.link}">..</a></td></tr>
  %endfor  
  </table>
</body>
</html>