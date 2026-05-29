# pliss.org

To build, you will need at a minimum:

  * python3
  * mako-1.1.0 or later

Simply type `make` and files will be read from `templates` and placed into `htdocs`.

`make serve` will build the website and start a simple HTTP server that you can
connect to and view the website. Pushing to the remote automatically makes the
changes live on the website (typically taking 10-20s).
