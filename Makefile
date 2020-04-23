install: server.install database.upgrade

start: server.start 

daemon: server.daemon 

stop: server.stop 

@PHONY: initialize
initialize: server.install database.upgrade server.start

include makefiles/server.mk
include makefiles/test.mk
include makefiles/database.mk