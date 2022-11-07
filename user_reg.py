#!C:/Users/DELL/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, cgitb;cgitb.enable()
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="mobile")
cur = conn.cursor()

print("""
<html>  
<head>   
<title>User registration</title>
<link rel="stylesheet" type="text/css" href="styles/styles1.css">
<link  rel="icon" type="logo/icon" href="logo.jpg">
<link rel="stylesheet" type="text/css" href="styles/css/bootstrap.min.css">
<script src="styles/js/jquery.min.js"></script>
<script src="styles/js/bootstrap.min.js"></script>
<style>
	* {box-sizing: border-box;}

body { 
  margin: 0;
  font-family: Verdana,Grande,Fahoma,sans-serif;
}

.header {
  overflow: hidden;
  background-color:mediumseagreen;
  padding: 3px 10px;
}

.header a {
  float: left;
  color: blue;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px; 
  line-height: 25px;
  border-radius: 4px;
}

.header a.logo {
  font-size: 25px;
  font-weight: bold;
}

.header a:hover {
  background-color: #ddd;
  color: black;
}

.header a.active {
  background-color: dodgerblue;
  color: white;
}

.header-right {
  float: right;
}

@media screen and (max-width: 500px) {
  .header a {
    float: none;
    display: block;
    text-align: left;
  }

  .header-right {
    float: none;
  }
}

	body{
		margin:0px;
		padding:0px;
		background-image:url('logo.jpg');
		background-repeat:no-repeat;
		background-size:100% 100%;
		background-size:cover;
		}
	.simple-form{
		text-align:center;
		margin:100px 400px;
		}
	#registration{
		margin:auto;
		width:80%;
		background-color:gray;
		text-align:center;
		color:white;
		opacity:0.8;
		border:2px solid white;
		padding:50px 0px;
		}
	#button{
		width:250px;
		padding:10px;
		border-radius:5px;
		outline:0px;
		}
	#ph{
		outline:0px;
		width:70px;
		padding:10px;
		border-radius:5px;
	}
	#phone{
		width:200px;
		padding:10px;
		border-radius:5px;
		outline:0px;
		}
		#check{
	font-family:serif;
	font-size:18px;
}
	#rd{

	}
	#but{
		color:white;
		font-size:18px;
	}
	#butt{
		width:200px;
		padding:10px;
		border-radius:5px;
		outline:0px;
		background-color:#0c6996;
		border:2px solid #01010c;
		color:aliceblue;
		font-size:18px;
		}
        .container{
      border:1px solid white;
	background:seagreen;
	padding:9px;
	color:white;
	margin:10px auto;
	text-align:center;
	width:400px;
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
#submit:hover{
color:pink;
background:navy;

}


	</style>
</head>  
<body> 
<div class="header">
<img src="logo.jpg" alt="logo" width="70" height="70"
style="margin-left:5px;
margin-top:4px;
margin-bottom:4px;border-radius:50%">
<div class="google">
<h1 style="margin-left:90px; margin-top:-60px; font-family:times new roman;font-size:40">SARA MOBILES</h1>
 </div>
 </div><br><br><br><br><br>""")
print("""
 <center>
<div class="container"> 
<h3><br><b>REGISTRATION</b></h3>
<form action="#" method="post" enctype="multipart/form-data" >
<table style="color:black;font-family:cursive;">
<tr>
<td align="left"><b><br>UserID:</b></td>
<td><input type="text" name="uid" id="uid" required></td>
</tr>
<tr>
<td align="left"><b><br>Name:</b></td>
<td><input type="text" name="name" id="name" required></td>
</tr>
<tr>
<td align="left"><b><br>E-mail:</b></td>
<td><input type="email" placeholder="@gmail.com" name="gmail" id="gmail" required></td>
</tr>
<tr>
<td align="left"><b><br>DOB:</b></td>
<td><input type="date" name="dt" id="dt" required></td>
</tr>
<tr>
<td align="left"><b><br>Gender:</b></td>
<td><input type="radio" value="male" name="gen" id="gen">Male<input type="radio" value="female" name="gen" id="gen">Female</td>
</tr>
<tr>
<td align="left"><b><br>Mobile number:</b></td>
<td><input type="tel" name="number" id="number" required></td>
</tr>
<tr>
<td align="left"><b><br>Address:</b></td>
<td><input type="tel" name="address" id="address" required></td>
</tr>
<tr>
<td align="left"><b><br>Username:</b></td>""")
print("""
<td><input type="text" name="uname" id="uname" required></td>
</tr>
<tr>
<td align="left"><b><br>Password:</b></td>

<td><input type="password" name="psw" id="psw" required></td>
</tr>
<tr>
<td><b>Profile:</b></td>
<td><br><input type="file" id="profile" name="profile"></td>
</tr>


</table><br>
<input type="submit" name="submit" id="submit" value="Register" class="btn float-right login_btn">
<input type="reset" value="Cancel" class="btn float-right login_btn">
</form>
<a href="userlogin.py"><u><b>Existing user? Click to Login</b></u></a>
</div> 
</center>
</body>  
</html>  
""")
f = cgi.FieldStorage()
sub = f.getvalue("submit")
if sub != None:

    userid = f.getvalue("uid")
    name = f.getvalue("name")
    email = f.getvalue("gmail")
    dob = f.getvalue("dt")
    gender = f.getvalue("gen")
    mobno = f.getvalue("number")
    address = f.getvalue("address")
    username = f.getvalue("uname")
    password = f.getvalue("psw")
    profile = f['profile']
    if profile.filename:
        import os

        fp = os.path.basename(profile.filename)
        
    
        q = """insert into
        user_reg(uid,name,gmail,dt,gen,number,address,uname,psw,profile)
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(userid, name, email, dob, gender, mobno, address, username, password,fp)
        
        conn.commit()
        conn.close()

      

        print("""
                            <script>
                			    alert("Registered successfully");
                                location.href="userlogin.py";
                            </script>
                           """)
    else:
        print("""
                            <script>
                                alert("Login invalid");
                                location.href="user_reg.py";
                            </script>
                            """)