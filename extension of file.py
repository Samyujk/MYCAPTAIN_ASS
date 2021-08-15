filename=input(("Input the Filename: "))
name=filename.split(".")
extension=name[-1]
if extension=="py":
    print("The extension of the file is : 'python'")
else:
    print("The extension of the file is : '%s'"%(extension))
          
          
