from config import config

maincntr = config["main_controller"]
importfrom = maincntr["package"]+"."+maincntr["module"]
module = __import__(importfrom, globals(), locals(), maincntr["class"])

if __name__ == "__main__":
    main = module.Main()
    main.run()
