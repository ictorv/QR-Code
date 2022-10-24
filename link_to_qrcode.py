import pyqrcode
link="https://github.com/ictorv"
ob=pyqrcode.create(link)
ob.svg("Generated.svg",scale=20)
print(ob.terminal(quiet_zone=1))