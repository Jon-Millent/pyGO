import time
class Event(object):
    def __init__(self):
        self.lib={}
        self.id=999
         
    def on(self,type,fn):
        self.id+=1
        if not self.lib.get(type):
            self.lib[type]={}
    
        self.lib[type][self.id] = fn
        return self.id
         
    def  emit(self,type,id=500):
        if id != 500:
           if self.lib[type].get(id):
               self.lib[type].get(id)()
        else:     
            op =  self.lib[type]
            for i in op:
                op[i]()
    def remove(self,type,id=500):
        list = self.lib.get(type)
        if id!=500:
            if list:
                if list.get(id):
                    del list[id]
        else:
            if list:
                self.lib[type] = {}

aa = Event()
 
def show():
    print('sleeing ...')
    time.sleep(1)
    #aa.remove('click')
    print('sleeing ok')
def show2():
    print('aaaasssssss')   
def show3():
    print('aaaabbbbbbbbbb') 
idd = aa.on('click',show)
idd2 = aa.on('click',show2)
idd3 = aa.on('click',show3)

aa.remove('click',idd2)
aa.emit('click')
 
         
         

