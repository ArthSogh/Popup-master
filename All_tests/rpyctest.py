import rpyc
conn = rpyc.classic.connect("localhost")

rsys = conn.modules.sys     # remote module on the server!
minidom = conn.modules["xml.dom.minidom"]
