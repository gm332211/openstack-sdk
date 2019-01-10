import docker
client=docker.DockerClient(base_url='tcp://192.168.1.10:2375')
print(client.info())
# print(client.df())
for image in client.images.list():
    print(image,image.id)
    print(image.history())
    print(image.attrs)
    print(image.tags)