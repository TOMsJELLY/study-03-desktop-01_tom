import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def search_junction(word, location):
    # print(word + " from JavaScript")
    # print("a")
    return search.kimetsu_search(word, location)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)