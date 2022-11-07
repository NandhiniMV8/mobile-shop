#!C:/Users/DELL/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb;cgitb.enable()
print("""
<html>
<head>
	<title>User login</title>
	<style>
	*{
padding:0;
margin:0;
}
img{
border-radius:50%;
margin-left:40px;
margin-top:10px;
}
.header{
height:100px;
width:500%;
position:fixed;
background-color:mediumseagreen;
}
.google{
color:white;
position:absolute;
top:20%;
left:50px;
}
body{
		margin:0px;
		padding:0px;
		background-image:url('bg.jpg');
		background-repeat:no-repeat;
		background-size:100% 100%;
		background-size:cover;
		}

.form{
width:500px;
height:300px;
padding:30px;
position:absolute;
top:50%;
left:50%;
transform:translate(-50%, -50%);
background:rgba(0,0,0,0.8);
color:white;
text-align:center;
border-radius:20px;
font-size:1rem;
}
.header h3 {
	padding:30px;
}

.form input[type="text"],
.form input[type="password"] {
	border:1px solid white;
	background:none;
	padding:9px;
	color:white;
	margin:10px auto;
	text-align:center;
	width:170px;
	border-radius:20px;
	outline:none;
}

.form input[type='submit']{
padding: 7px 20px;
background: none;
outline:none;
color:white;
width:20px;
border-radius:20px;
}
.form input[type="text"]:focus,
.form input[type="password"]:focus {
border: 2px solid rgb(128,0,122);
}
.form input[type="submit"]:hover{
	border:0px;
	color:rgb(128,0,122);
	box-shadow:3px 3px 8px rgb(128,0,122);
}
.form input[type='reset']{
padding: 7px 20px;
background: none;
outline:none;
color:white;
width:80px;
border-radius:20px;
}
.form input[type="text"]:focus,
.form input[type="password"]:focus {
border: 2px solid rgb(128,0,122);
}
.form input[type="reset"]:hover{
	border:0px;
	color:rgb(128,0,122);
	box-shadow:3px 3px 8px rgb(128,0,122);
}
.form i{
	position:absolute;
	margin:15px 0px 0px -40px;
}
.visibility:hover {
	cursor:pointer;
}
.imgcontainer {
  text-align: center;
  margin-top:-100px;
  margin: 0px 0 0px 0;
}

.logo {
  width: 100px;
  height:100px;
  border-radius: 50%;
  position:absolute;
  margin-left:100px;
  top:-100px;
  left:205px;
}

.container {
  padding: 2px;
}
#submit{
width:150px;
margin-top:20px;
margin-left:80px;
}
#clear{
width:150px;
margin-top:20px;
margin-left:10px;
}
.forgot{
color:white;
margin-top:25px;
}
.forgot:hover{
color:violet;
}
	</style>
	<meta charset='utf-8'>
	<meta content='If-edge'>
	<title>Login 2</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel='stylesheet' type='text/css' media='screen' href='styles/main.css'>
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link  rel="icon" type="logo/icon" href="logo.jpg">
    <script src='styles/main.js'></script>
    
</head>
<body>
<div class="header">
<img src="logo.jpg" alt="logo" width="80" height="80">
<div class="google">
<h1 style="margin-left:90px; margin-top:-10px; font-family:times new roman;font-size:35">SARA MOBILES</h1> </div>
 </div>

			<div class="form">
				<form>
				 <img src="logo.jpg" alt="logo" class="logo"><br><br><br>
					
							<span class="input-group-text"><i class="fas fa-user"></i></span>
						
						<a>USERNAME:<input type="text" name="uname" id="uname" class="form-control" placeholder="username"><br>

					
					
							<span class="input-group-text"><i class="fas fa-key"></i></span>
						
						<a>PASSWORD:</a><input type="password" name="pwd" id="pwd" class="form-control" placeholder="password">
					
					
					
						<table>
					<td>	<input type="submit" id="submit" name="submit" value="Login"></td>
					
						<td><input type="submit" id="clear" name="submit" value="clear"></td>
						</table><br><br>
									<a href="#" class="forgot">Forgot your password?</a><br>
                                    <br>
      <p>Don't have an account?<a href="user_reg.py" class="sign">Sign Up</a></p>
				</form>
			</div>
		</div>
	</div>
</div>
</body>
</html>
""")
conn = pymysql.connect(host="localhost", user="root", password="", database="mobile")
cur = conn.cursor()
f = cgi.FieldStorage()
username = f.getvalue("uname")
password = f.getvalue("pwd")
v = f.getvalue("submit")
if v != None:

    q = """select * from user where username='%s' and password='%s'""" % (username, password)
    cur.execute(q)
    r = cur.fetchone()
    if r != None:
        print("""
                    <script>
        			alert("Login successful");
                    location.href="user_dashboard.html";
                    </script>
                """ )
    else:
        print("""
                    <script>
                    alert("Login invalid");
                    location.href="userlogin.py";
                    </script>
                """)