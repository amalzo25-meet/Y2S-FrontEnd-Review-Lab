from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return ('''<html>
        <h1>Welcome!</h1>
        <p>This is a photo gallery containing the most interesting things in the world,food, pets, and outer space!
        <br><a href='/food1'>go to the first food photo</a><br>
        <a href='/food2'>go to the second food photo</a><br>
        <a href='/pet2'>go to the second pet photo</a><br>
        <a href='/space1'>go to the first space photo</a>
        <br><h4>If you want to be directed to a room instantly, choose the room you want to go to:</h4>
        <form>
        <input type="radio" name="room" value="food1"  onclick="window.location.href = '/food1'">Food1
        <br><input type="radio" name="room" value="food2"  onclick="window.location.href = '/food2'">Food2
        <br><input type="radio" name="room" value="food3"  onclick="window.location.href = '/food3'">Food3
        <br><input type="radio" name="room" value="pet1"  onclick="window.location.href = '/pet1'">Pet1
        <br><input type="radio" name="room" value="pet2"  onclick="window.location.href = '/pet2'">Pet2
        <br><input type="radio" name="room" value="pet3"  onclick="window.location.href = '/pet3'">Pet3
        <br><input type="radio" name="room" value="space1"  onclick="window.location.href = '/space1'">Space1
        <br><input type="radio" name="room" value="space2"  onclick="window.location.href = '/space2'">Space2
        <br><input type="radio" name="room" value="space3"  onclick="window.location.href = '/space3'">Space3
        </form>
        </html> ''')


@app.route('/food1')
def food1():
    return ('''<html><h1>Food1</h1><br>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpKqIXGk1wIr3NMpYbJy9VLwH-38e0NyeExA&s"  width="400px">
            <p>(I feel so sad looking at this food while eating iasa food)</p>
            <a href='/food2'>go to the second food photo</a><br>
            <a href='/food3'>go to the third food photo</a><br>
            <a href='/'>go to the home page</a></html>''')


@app.route('/food2')
def food2():
    return ('''<html><h1>Food2</h1><br>
            <img src="https://blog.remitly.com/wp-content/uploads/2023/09/jordan-mansaf-scaled.jpg" width="400px">
            <p>(im hungry)</p><br>
            <a href='/food1'>go to the first food photo</a><br>
            <a href='/food3'>go to the third food photo</a><br>
            <a href='/'>go to the home page</a></html>''')



@app.route('/food3')
def food3():
    return ('''<html><h1>Food3</h1><br>
            <img src="https://cardamomandtea.com/wp-content/uploads/2021/09/IMG_1320-min.jpg" width="400px">
            <p>(im hungry)</p><br>
            <a href='/food1'>go to the first food photo</a><br>
            <a href='/food2'>go to the second food photo</a><br>
            <a href='/'>go to the home page</a></html>''')



@app.route('/pet1')
def pet1():
    return ('''<html><h1>pet1</h1><br>
            <img src="https://www.wfla.com/wp-content/uploads/sites/71/2023/05/GettyImages-1389862392.jpg?w=2560&h=1440&crop=1" width="400px">
            <br>
            <a href='/pet2'>go to the second pet photo</a><br>
            <a href='/pet3'>go to the third pet photo</a><br>
            <a href='/'>go to the home page</a></html>''')


@app.route('/pet2')
def pet2():
    return ('''<html><h1>pet2</h1><br>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWWAZgBBqrUpeUyd7vpqYk74m67UicGnlL8Q&s" width="400px">
            <br>
            <a href='/pet1'>go to the first pet photo</a><br>
            <a href='/pet3'>go to the third pet photo</a><br>
            <a href='/'>go to the home page</a></html>''')



@app.route('/pet3')
def pet3():
    return ('''<html><h1>pet3</h1><br>
            <img src="https://preview.redd.it/jx4h468iyoo51.jpg?width=640&crop=smart&auto=webp&s=c406fd1945da950f15d6f246bcbba3570e82cace" width="400px">
            <br>
            <a href='/pet1'>go to the first pet photo</a><br>
            <a href='/pet2'>go to the second pet photo</a><br>
            <a href='/'>go to the home page</a></html>''')



@app.route('/space1')
def space1():
    return ('''<html><h1>Space1</h1><br>
            <img src="https://static.sciencelearn.org.nz/images/images/000/001/987/embed/AST_CNT_INT_M18galaxy.jpg?1674167306" width="400px">
            <br>
            <a href='/space2'>go to the second pet photo</a><br>
            <a href='/space3'>go to the third pet photo</a><br>
            <a href='/'>go to the home page</a></html>''')




@app.route('/space2')
def space2():
    return ('''<html><h1>space2</h1><br>
            <img src="https://c02.purpledshub.com/uploads/sites/41/2020/03/GettyImages-475158333-c-2e71c50-scaled.jpg" width="400px">
            <br>
            <a href='/space1'>go to the first space photo</a><br>
            <a href='/space3'>go to the third space photo</a><br>
            <a href='/'>go to the home page</a></html>''')


@app.route('/space3')
def space3():
    return ('''<html><h1>space3</h1><br>
            <img src="https://media.wired.com/photos/5a593a7ff11e325008172bc2/master/pass/pulsar-831502910.jpg" width="400px">
            <br>
            <a href='/space1'>go to the first space photo</a><br>
            <a href='/space2'>go to the second space photo</a><br>
            <a href='/'>go to the home page</a></html>''')




if __name__ == '__main__':
    app.run(debug=True)