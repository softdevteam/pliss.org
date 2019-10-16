<%page args="title=None, extra_css=None"/>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>
%if title:
	PLISS: ${title}
%else:
	PLISS
%endif
</title>
%if extra_css:
%    for css in extra_css:
	 <link href="${css}" rel="stylesheet" type="text/css" />
%    endfor
%endif

<body>
