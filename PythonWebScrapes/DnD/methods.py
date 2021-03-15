# modules.py
import requests
import json
import urls

def rawData(url):#
     # Get RAW Data file to work with
    res = requests.get(url)
    j_res = res.json()
    j_res = json.dumps(j_res)

    with open('DungeonsAndDragons.json','w') as jsonFile:
        jsonFile.write(j_res)
    return

def spell_index(url):
    rawData(url)
    spell_list = []
    with open('DungeonsAndDragons.json','r') as f:
        data = json.load(f)
        for i in data:
            if i == 'results':
                i_data = (data[i])
                for k in i_data:
                    spell_list.append(k['name'])

    with open('spellList.txt', 'w') as spells:
        for spellItem in spell_list:
            spells.write(f'{spellItem}\n')


def class_index(url):
    rawData(url)
    class_list = []
    with open('DungeonsAndDragons.json','r') as f:
        data = json.load(f)
        for i in data:
            if i == 'results':
                i_data = (data[i])
                for k in i_data:
                    class_list.append(k['name'])
                    url = url +'/'+ k['index']
                    print('url: ', url)
                    url = urls.url + str('classes')

    with open('classList.txt', 'w') as classes:
        for classItem in class_list:
            classes.write(f'{classItem}\n')


def races_index(url):
    rawData(url)
    races_list = []
    with open('DungeonsAndDragons.json','r') as f:
        data = json.load(f)
        for i in data:
            if i == 'results':
                i_data = (data[i])
                for k in i_data:
                    races_list.append(k['name'])
                    url = url +'/'+ k['index']
                    print('url: ', url)
                    url = urls.url + str('races')

    with open('racesList.txt', 'w') as races:
        for raceItem in races_list:
            races.write(f'{raceItem}\n')

def monsters_index(url):
    rawData(url)
    monsters_list = []
    with open('DungeonsAndDragons.json','r') as f:
        data = json.load(f)
        for i in data:
            if i == 'results':
                i_data = (data[i])
                for k in i_data:
                    monsters_list.append(k['name'])
                    url = url +'/'+ k['index']
                    print('url: ', url)
                    url = urls.url + str('races')

    with open('monstersList.txt', 'w') as monsters:
        for monsterItem in monsters_list:
            monsters.write(f'{monsterItem}\n')


