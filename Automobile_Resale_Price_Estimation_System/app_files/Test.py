'''
Created on 20-Feb-2022

@author: Srijan-PC
'''

from flask import Flask

app= Flask(__name__)

@app.route('/')

def dir_listing():   
    #filename = os.path.join(app.instance_path, 'my_folder', 'my_file.txt')
    #print(filename)
    return

# main function
if __name__ == '__main__':
    app.run(debug=True)
    
    