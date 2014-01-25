homePage='''
            <div style=" width:500px; margin:0 auto 0 auto;">
            </ol><hr>
            <form action="/pFound" method=post>
            <br><input type=submit value="Found">
            </form>
            <div sytle="float:right">
            <form action="/pMissing" method=post>
            <br><input type=submit value="Missing">
            </form>
            </div>
           </div> 
       '''
pMissingPage='''
<!DOCTYPE html> 
<html>

<head>
  <title>Gumshuda</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <style type="text/css">
    @font-face { 
  font-family: News Cycle; 
    src: url('../fonts/NewsCycle-Regular.eot'); 
    src: local("News Cycle"), url('../fonts/NewsCycle-Regular.ttf'); 
} 

html
{ height: 100%;}

*
{ margin: 0;
  padding: 0;}

body
{ font: normal 90% Arial, Helvetica, sans-serif;
  color: #000;
  background: #FFF;
}

/* tell the browser to render HTML 5 elements as block */
article, aside, figure, footer, header, hgroup, nav, section { 
  display:block;
}

p
{ padding: 0 0 10px 0;
  line-height: 1.7em;
  font-size: 100% }

img
{ border: 0;}

h1, h2, h3, h4, h5, h6 
{ font: normal 150% 'News Cycle', Arial, sans-serif;
  color: #3E9C6A;
  text-shadow: 1px 1px #000;
  margin: 10px 0 10px 0;}

h2
{ font: normal 150% 'News Cycle', Arial, sans-serif;}

h3
{ font: normal 120% 'News Cycle', Arial, sans-serif;}

h4, h5, h6
{ margin: 0;
  padding: 0 0 0px 0;
  font: normal 120% 'News Cycle', Arial, sans-serif;
  color: #FFF;
  line-height: 1.5em;}

h5, h6
{ font: normal 95% 'News Cycle', Arial, sans-serif;
  color: #888;
  padding-bottom: 15px;}
  
span
{ color: #000;}

a, a:hover
{ color: #000;
  background: transparent;
  outline: none;
  text-decoration: underline;}

a:hover
{ text-decoration: none;}

ul
{ margin: 2px 0 22px 30px;
  line-height: 1.7em;
  font-style: normal;
  font-size: 100%;}

ol
{ margin: 8px 0 22px 20px;}

ol li
{ margin: 0 0 11px 0;}

#main, header, #banner, #menubar, #site_content, footer, #content_grey, nav, #header_section
{ margin-left: auto; 
  margin-right: auto;}
  
header
{ position: relative;
  background: #F2F2F2 url(../images/background.jpg) repeat;
  height: 100px;
  border-bottom: 1px solid #DDD;} 
  
#header_section
{ width: 940px;
  height: 60px;
  margin-bottom: 20px;} 
  
#welcome
{ width: 310px;
  float: left;
  margin: 0 auto;
  padding: 10px 0 10px 0;
  background: transparent;} 
   
#welcome h2
{ font: normal 260% 'News Cycle', Arial, sans-serif;
  letter-spacing: -2px;
  text-shadow: 1px 1px #000;
  color: #3E9C6A;}
  
nav
{ width: 630px;
  height: 50px;
  margin-top: 42px;
  float: right;}   
  
ul#nav
{ margin:0;
  float: right;}

ul#nav li
{ padding: 0 0 0 0px;
  list-style: none;
  margin: 2px 0 0 0;
  display: inline;
  text-align: center;   
  background: transparent;}

ul#nav li a
{ font: normal 110% Arial, Helvetica, sans-serif;
  height: 24px;
  margin: 10px 0 0 20px;
  padding: 6px 10px 6px 10px;
  background: transparent; 
  text-align: center;
  color: #000;
  text-shadow: 1px 1px #FFF;  
  text-decoration: none;} 
  
ul#nav li.current a, ul#nav li:hover a
{ text-shadow: 1px 1px #000;
  color: #FFF;
  background: #3E9C6A;
  background: -moz-linear-gradient(#ABDFC3, #3E9C6A);
  background: -o-linear-gradient(#ABDFC3, #3E9C6A);
  background: -webkit-linear-gradient(#ABDFC3, #3E9C6A);
  border-radius: 7px 7px 7px 7px;
  -moz-border-radius: 7px 7px 7px 7px;
  -webkit-border: 7px 7px 7px 7px;}

#site_content
{ width: 940px;
  padding-top: 20px;
  overflow: hidden;
  margin-bottom: 30px;} 

.sidebar_container
{ float: left;
  width: 240px;
  padding: 0;
  color: #000;}

.sidebar
{ float: left;
  width: 240px;
  margin: 0 0 10px 0;}

.sidebar_item
{ width: 220px;}

.sidebar h2
{ padding: 5px 0 0 0;
  font: normal 150% 'News Cycle', Arial, sans-serif;
  height: 30px;
  text-shadow: none;
  color: #000;} 

#content
{ width: 940px;
  margin: 0 10px 20px 0;
  float: left;}

.content_item
{ float: right;
  width: 690px;
  margin-bottom: 20px;}
 
.content_imagetext
{ width: 660px;
  padding: 5px;
  margin: 20px 0 0 0;
  float: left;}
 
.content_image
{ float: left; 
  width: 150px;
  height: 150px;
  margin: 0 20px 10px 0;}
  
.content_container
{ width: 320px;
  padding: 5px;
  margin: 20px 10px 0 0;
  float: left;}
  
footer
{ padding: 30px 0px;
  font-weight: normal;
  text-align: center; 
  text-shadow: 1px 1px #FFF;
  color: #000;
  background: #F2F2F2;}

footer a
{ color: #000;
  text-decoration: none;
  padding-bottom: 20px;}

footer a:hover
{ text-decoration: underline;
  color: #000;}
 
 .button_small
{ font: normal 110% Arial, Helvetica, sans-serif;
  float: left;
  padding: 5px 15px 7px 10px;
  border: 1px solid #FFF; 
  background: #3E9C6A;
  background: -moz-linear-gradient(#ABDFC3, #3E9C6A);
  background: -o-linear-gradient(#ABDFC3, #3E9C6A);
  background: -webkit-linear-gradient(#ABDFC3, #3E9C6A);
  border-radius: 7px 7px 7px 7px;
  -moz-border-radius: 7px 7px 7px 7px;
  -webkit-border: 7px 7px 7px 7px;
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0px 0px 5px;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0px 0px 5px;
  box-shadow: rgba(0, 0, 0, 0.5) 0px 0px 5px;}
  
.button_small a
{ color: #FFF;
  padding-left: 5px;
  text-shadow: 1px 1px #000;}

.form_settings
{ margin: 15px 0 0 0;}

.form_settings p
{ padding: 0 0 4px 0;}

.form_settings span
{ float: left; 
  width: 280px; 
  text-align: left;
  text-shadow: none;}
  
.form_settings input, .form_settings textarea
{ padding: 2px; 
  width: 299px; 
  font: 100% arial; 
  border: 1px solid #E5E5DB; 
  background: #FFF; 
  color: #47433F;}
  
.form_settings input[type="checkbox"]
{ padding: 2px 0; 
  width: 15px; 
  font: 100% arial; 
  border: 0; 
  background: #FFF; 
  color: #47433F;
  margin: 28px 0;}

.form_settings .submit
{ font: 100% arial; 
  border: 1px solid #FFF; 
  width: 99px; 
  margin: 0 0 0 206px; 
  height: 26px;
  padding: 2px 0 3px 0;
  cursor: pointer; 
  background: #3E9C6A;
  background: -moz-linear-gradient(#ABDFC3, #3E9C6A);
  background: -o-linear-gradient(#ABDFC3, #3E9C6A);
  background: -webkit-linear-gradient(#ABDFC3, #3E9C6A);
  border-radius: 7px 7px 7px 7px;
  -moz-border-radius: 7px 7px 7px 7px;
  -webkit-border: 7px 7px 7px 7px;
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0px 0px 5px;
  -moz-box-shadow: rgba(0, 0, 0, 0.5) 0px 0px 5px;
  box-shadow: rgba(0, 0, 0, 0.5) 0px 0px 5px;
  color: #FFF;
  text-shadow: 1px 1px #000;}

.slideshow
{ width: 690px;
  height: 300px;
  margin-top: 20px;
  float: left;}  
  
/* styling for the slideshow on the homepage */
ul.slideshow {
  list-style: none;
  width: 690px;
  height: 300px;
  overflow: hidden;
  position: relative;
  margin: 0;}
  
ul.slideshow li {
  position: absolute;
  margin: 0;
  padding: 0;
  left: 0;
  right: 0;}
 
ul.slideshow li.show {
  z-index: 500;}
 
ul img {
  border: none;}
 
#slideshow-caption {
  width: 690px;
  height: 42px;
  position: absolute;
  bottom: 0;
  left: 0; 
  z-index: 500;}
 
#slideshow-caption .slideshow-caption-container {
  padding: 10px 25px 10px 25px; 
  background: transparent url(../images/transparent.png) repeat;  
  z-index: 1000;}
 
#slideshow-caption p {
  padding: 0;
  font: normal 130% arial, sans-serif;
  color: #FFF;
  text-shadow: 1px 1px #000;}
 
 
    
    </style>
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
</head>

<body>
  <div id="main">
	
	<header>
	  
	  <div id="header_section">	  
	    
		<div id="welcome">
	      <h2>Gumshuda</h2>
	    </div><!--close welcome-->			  	
	  
	    <nav>
          <ul id="nav">
         <!--   <li><a href="index.html">Home</a></li>
            <li><a href="ourwork.html">Our Work</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>
            <li><a href="projects.html">Projects</a></li>
			<li><a href="contact.html">Contact Us</a></li>-->
            <li class="current"><a href="contact.html">Add Person</a></li>
          </ul>
        </nav>
      
	  </div>		
	
	</header>
    
	<div id="site_content">
	
	  <div id="content">
	
        <h2>Add Person</h2>
        <p>Add the information of a missing person.</p>
		  <div class="content_item">
		  <!-- Image Upload -->
  <style>
#holder { border: 10px dashed #ccc; width: 200px; min-height: 200px; margin: 20px auto;}
#holder.hover { border: 10px dashed #0c0; }
#holder img { display: block; margin: 10px auto; width: 200px;}
#holder p { margin: 10px; font-size: 14px; }
progress { width: 200;}
progress:after { content: '%'; }
.fail { background: #c00; padding: 2px; color: #fff; }
.hidden { display: none !important;}
</style>
<article>
  <div id="holder">
  </div> 
  <p id="upload" class="hidden"><label>Drag & drop not supported, but you can still upload via this input field:<br><input type="file"></label></p>
  <p id="filereader">File API & FileReader API not supported</p>
  <p id="formdata">XHR2's FormData is not supported</p>
  <p id="progress">XHR2's upload progress isn't supported</p>
  <!-- <p>Upload progress: <progress id="uploadprogress" min="0" max="100" value="0">0</progress></p> -->
  
</article>
<script>
var holder = document.getElementById('holder'),
    tests = {
      filereader: typeof FileReader != 'undefined',	
      dnd: 'draggable' in document.createElement('span'),
      formdata: !!window.FormData,
      progress: "upload" in new XMLHttpRequest
    }, 
    support = {
      filereader: document.getElementById('filereader'),
      formdata: document.getElementById('formdata'),
      progress: document.getElementById('progress')
    },
    acceptedTypes = {
      'image/png': true,
      'image/jpeg': true,
      'image/gif': true
    },
    progress = document.getElementById('uploadprogress'),
    fileupload = document.getElementById('upload');

"filereader formdata progress".split(' ').forEach(function (api) {
  if (tests[api] === false) {
    support[api].className = 'fail';
  } else {
    // FFS. I could have done el.hidden = true, but IE doesn't support
    // hidden, so I tried to create a polyfill that would extend the
    // Element.prototype, but then IE10 doesn't even give me access
    // to the Element object. Brilliant.
    support[api].className = 'hidden';
  }
});

function previewfile(file) {
  if (tests.filereader === true && acceptedTypes[file.type] === true) {
    var reader = new FileReader();
    reader.onload = function (event) {
      var image = new Image();
      image.src = event.target.result;
      image.width = 250; // a fake resize
      holder.appendChild(image);
    };

    reader.readAsDataURL(file);
  }  else {
    holder.innerHTML += '<p>Uploaded ' + file.name + ' ' + (file.size ? (file.size/1024|0) + 'K' : '');
    console.log(file);
  }
}

function readfiles(files) {
    debugger;
    var formData = tests.formdata ? new FormData() : null;
    for (var i = 0; i < files.length; i++) {
      if (tests.formdata) formData.append('file', files[i]);
      previewfile(files[i]);
    }

    // now post a new XHR request
    if (tests.formdata) {
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/devnull.php');
      xhr.onload = function() {
        progress.value = progress.innerHTML = 100;
      };

      if (tests.progress) {
        xhr.upload.onprogress = function (event) {
          if (event.lengthComputable) {
            var complete = (event.loaded / event.total * 100 | 0);
            progress.value = progress.innerHTML = complete;
          }
        }
      }

      xhr.send(formData);
    }
}

if (tests.dnd) { 
  holder.ondragover = function () { this.className = 'hover'; return false; };
  holder.ondragend = function () { this.className = ''; return false; };
  holder.ondrop = function (e) {
    this.className = '';
    e.preventDefault();
    readfiles(e.dataTransfer.files);
  }
} else {
  fileupload.className = 'hidden';
  fileupload.querySelector('input').onchange = function () {
    readfiles(this.files);
  };
}

</script>
 <!-- File Upload End -->
		    
			<div class="form_settings">           
                            <form action="/missing" method=post>
			  <p><span>Name</span><input class="contact" type="text" name="name" value="" /></p>
			  <p><span>Age</span><input class="contact" type="text" name="age" value="" /></p>
			  <p><span>Last Known Place</span><input class="contact" type="text" name="lkPlace" value="" /></p>
			  <p><span>Height</span><input class="contact" type="text" name="height" value="" /></p>
			  <p><span>Hair Color</span><!--<input class="contact" type="text" name="hColor" value="" /></p> --><select>
  <option value="Brunette">Black</option>
  <option value="Blonde">Brown</option>
  <option value="Grey">Grey</option>
</select>
			  <p><span>Skin Color</span><input class="contact" type="text" name="sColor" value="" /></p>
			  <p><span>Eye Color</span><!--<input class="contact" type="text" name="eColor" value="" /></p> --><select> <option value="Black">Black</option>
  <option value="Brown">Brown</option>
  <option value="Blue">Blue</option>
  <option value="Grey">Grey</option></select>
			  <p><span>Possible Speaking Abilities</span><input class="contact" type="text" name="psAbilities" value="" /></p>
			  <p><span>Possible Speaking Names</span><input class="contact" type="text" name="psNames" value="" /></p>
			  <p><span>Contact Number</span><input class="contact" type="text" name="cNumber" value="" /></p>
			  <p><span>Contact Info</span><input class="contact" type="text" name="cInfo" value="" /></p>
			  <p><span>ID Card Number</span><input class="contact" type="text" name="idNo" value="" /></p>
			  <p><span>Clothing Type</span><input class="contact" type="text" name="cType" value="" /></p>
			  <p><span>Clothing Color</span><input class="contact" type="text" name="cColor" value="" /></p>
              <p style="padding: 10px 0 10px 0;">Please enter the answer to this simple maths question (to prevent spam)</p>
			  <p><span>Maths Question: 9 + 3 = ?</span><input type="text" name="user_answer" class="contact" /><input type="hidden" name="answer" value="4d76fe9775" /></p>
              <p style="padding-top: 15px"><span>&nbsp;</span><input class="submit" type="submit" name="contact_submitted" value="Send" /></p>
            </div><!--close form_settings-->
                          </form>
		  </div><!--close content_item-->	
      
	  </div><!--close content-->   
	
	</div><!--close site_content-->  	
  
    <footer>
	  
    </footer>   
  
  </div><!--close main-->

  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/image_slide.js"></script>	
  
    
  
  
</body>
</html>

'''








pFoundPage='''
            </ol><hr>
            <form action="/found" method=post>
            <textarea name=content rows=3 cols=60></textarea>
            <br><input type=submit value="Found">
            </form>       '''





temp='''
            </ol><hr>
            <form action="/missing" method=post>
            <textarea name=content rows=3 cols=60></textarea>
            <br><input type=submit value="Missing">
            </form>
       '''



















from google.appengine.ext import db
import webapp2

class Greeting(db.Model):
    name = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    age = db.StringProperty(multiline=True)
    lkPlace = db.StringProperty(multiline=True)
    height = db.StringProperty(multiline=True)
    doMissing = db.StringProperty(multiline=True)
    hColor = db.StringProperty(multiline=True)
    sColor = db.StringProperty(multiline=True)
    eColor = db.StringProperty(multiline=True)
    psAbilities = db.StringProperty(multiline=True)
    psNames = db.StringProperty(multiline=True)
    cNumber = db.StringProperty(multiline=True)
    pic = db.StringProperty(multiline=True)
    cInfo = db.StringProperty(multiline=True)
    idNo = db.StringProperty(multiline=True)
    cType = db.StringProperty(multiline=True)
    cColor = db.StringProperty(multiline=True)
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        greetings = db.GqlQuery("SELECT * FROM Greeting")
 #       greetings = Greeting.all()
#        for greeting in greetings:
#            greeting.delete()
#           self.response.write('<li> %s' % greeting.age)
        self.response.write(homePage)


class pMissing(webapp2.RequestHandler):
    def post(self):
        self.response.write(pMissingPage)

class pFound(webapp2.RequestHandler):
    def post(self):
        self.response.write(pFoundPage)


class Found(webapp2.RequestHandler):
    def post(self):
        gree = self.request.get('content')
        greetingss=Greeting.all()
        fou=0
        for temp in greetingss:
            if(temp.name==gree):
                    self.response.write('yes')
                    fou=1
        if(fou!=1):
            self.response.write('no')


class Missing(webapp2.RequestHandler):
    def post(self):
        greeting = Greeting(

        name = self.request.get('name'),
        date = self.request.get('date'),
        age = self.request.get('age'),
        lkPlace = self.request.get('lkPlace'),
        height = self.request.get('height'),
        doMissing = self.request.get('doMissing'),
        hColor = self.request.get('hColor'),
        sColor = self.request.get('sColor'),
        eColor = self.request.get('eColor'),
        psAbilities = self.request.get('psAbilities'),
        psNames = self.request.get('psNames'),
        cNumber = self.request.get('cNumber'),
        pic = self.request.get('pic'),
        cInfo = self.request.get('cInfo'),
        idNo = self.request.get('idNo'),
        cType = self.request.get('cType'),
        cColor = self.request.get('cColor')
            )
        greeting.put()
        self.redirect('/')





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/pFound', pFound),
    ('/pMissing', pMissing),
    ('/found', Found),
    ('/missing', Missing)
], debug=True)
