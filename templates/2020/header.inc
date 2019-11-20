<%page args="title=None, extra_css=None"/>
<!DOCTYPE HTML>
<!--
	Spatial by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>
%if title:
	PLISS: ${title}
%else:
    PLISS
%endif
        </title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" />
        <link rel="icon" type="image/png" href="favicon.ico">
	</head>
    <body${ ' class="landing"' if page=='index' else '' }>

		<!-- Header -->
			<header id="header" ${ 'class="alt"' if page=='index' else '' }>
				<h1><strong><a href="index.html"><img src="images/pliss-logo-col.png" style="height: 50px; vertical-align: middle; margin-left: 1em" /></a></strong></h1>
				<nav id="nav">
					<ul>
						<li><a href="index.html">Home</a></li>
						<li><a href="lectures.html">Lectures</a></li>
						<li><a href="location.html">Location</a></li>
						<li><a href="organisers.html">Organisers</a></li>
						<li><a href="registration.html">Registration</a></li>
						<li><a href="speakers.html">Speakers</a></li>
					</ul>
				</nav>
			</header>

			<a href="#menu" class="navPanelToggle"><span class="fa fa-bars"></span></a>
