import cocos

cocos.director.director.init()

scene = cocos.scene.Scene()

label = cocos.text.Label("Hello World!", position=(100, 200))

scene.add(label)

action = cocos.actions.MoveBy((200, 0), 3)

label.do(cocos.actions.Repeat(action + cocos.actions.Reverse(action)))

cocos.director.director.run(scene)