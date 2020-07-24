import pandas as pd
import wikipedia
import csv
import time

namelist = ["Aardvark","Aardwolf","African Elephant","African Tree Pangolin","Alligator","Alpaca","Anemone","Anteater","Antelope","Apes","Armadillo","Arthropod","Asian Elephant","Aye-Aye","Baboon","Badger","Bandicoot","Bat","Bearded Dragon","Beaver","Beluga Whale","Bengal Tiger","Big-Horned Sheep","Billy Goat","Bird","Bison","Black Bear","Black Footed Rhino","Black Howler Monkey","Black Rhino","Blacktip Reef Shark","Blue Shark","Blue Whale","Boar","Bob-Cat","Bonobo","Bottlenose Dolphin","Bottlenose Whale","Brown Bear","Buffalo","Bull","Bull frog","Caiman Lizard","Camel","Capuchin Monkey","Capybara","Caribou","Cat","Cattle","Cheetah","Chimpanzee","Chinchilla","Chipmunk","Common Dolphin","Common Seal","Coral","Cougar","Cow","Coyote","Crocodile","Crustacean","Dart Frog","Deer","Degus","Dik-Dik","Dingo","Dog","Dogfish Shark","Dolphin","Donkey","Dormouse","Draft Horse","Duckbill Platypus","Dugong","Dusky Shark","Elephant","Elephant Seal","Elk","Ermine","Eurasian Lynx","Ferret","Fish","Florida Panther","Flying Fox","Fox","Fresh Water Crocodile","Frog","Fur Seal","Galapagos Land Iguana","Galapagos Shark","Galapagos Tortoise","Gazelle","Gecko","Giant Anteater","Giant Panda","Gibbon","Giraffe","Goat","Gopher","Gorilla","Gray Fox","Gray Nurse Shark","Gray Reef Shark","Gray Whale","Great White Shark","Green Poison Dart Frog","Green Sea Turtle","Grizzly Bear","Groundhog","Guinea Pig","Hairy-Nosed Wombat","Hammerhead Shark","Harbor Porpoise","Harbor Seal","Hare","Harp Seal","Hawaiian Monk Seal","Hedgehog","Hippopotamus","Horn Shark","Horse","Howler Monkey","Humpback Whale","Hyena","Hyrax","Iguana","Iguanodon","Impala","Insect","Irrawaddy Dolphin","Jackal","Jackrabbit","Jaguar","Jellyfish","Kangaroo","Kermode Bear","Killer Whale","Koala","Komodo Dragon","Kookaburra","Lama","Lamb","Lancelet","Least Weasel","Leatherback Sea Turtle","Lemming","Lemon Shark","Lemur","Leopard","Leopard Gecko","Leopard Seal","Leopard Shark","Lion","Llama","Loggerhead Turtles","Lynx","Mako Shark","Manatee","Manta Ray","Mantis","Marbled Salamander","Marmot","Marsupial","Meerkat","Megamouth Shark","Melon-Headed Whale","Miniature Donkey","Mink","Minke Whale","Mole","Mole Salamander","Mollusk","Mongoose","Monitor Lizard","Monk Seal","Monkey","Moose","Mountain Lion","Mouse","Mule","Muskox","Muskrat","Naked Mole Rat","Narwhal","Nautilus","Newt","Northern Right Whale","Nurse Shark","Nutria","Nyala","Ocelot","Octopus","Okapi","Opossum","Orangutan","Orca","Otter","Ox","Panda","Panther","Pig","Pilot Whale","Pine Marten","Platypus","Polar Bear","Porcupine","Porpoise","Possum","Potbellied Pig","Potto","Prairie Dog","Proboscis Monkey","Przewalski's Wild horse","Puma","Pygmy Hippopotamus","Pygmy Right Whale","Pygmy Sperm Whale","Quokkas","Quolls","Rabbit","Raccoon","Rat","Ray","Red Fox","Red Kangaroo","Red Panda","Red-Eyed Tree Frog","Reef Shark","Reindeer","Rhino","Rhinoceros","Right Whale","Ringed Seal","Risso's Dolphin","River Dolphin","Salamander","Sandbar Shark","Scalloped Hammerhead Shark","Sea Lion","Sea Turtles","Seal","Sei Whale","Shark","Sheep","Shortfin Mako Shark","Siberian Tiger","Silky Shark","Skink","Skunk","Slender Loris","Sloth","Sloth Bear","Snake","Snow Fox","Snow Hare","Snow Leopard","Snow Monkey","Somali Wild Ass","Spectacled Bear","Sperm Whale","Spider Monkey","Spiny Dogfish Shark","Spotted Dolphin","Squirrel","Star-Nosed Mole","Stellar Sea Lion","Striped Dolphin","Sun Bear","Takin","Tamarin","Tapir","Tasmanian Devil","Tasmanian Tiger","Terrapin","Thresher Shark","Tiger","Tiger Salamander","Tiger Shark","Topi","Tortoise","Tree Frog","Turtle","Uakari","Vampire Bat","Vancouver Island Marmot","Vervet Monkey","Vicuna","Vole","Wallaby","Walrus","Warthog","Water Buffalo","Weasel","Whale Shark","Whale","White Rhino","White Tailed Deer","White-Beaked Dolphin","Whitetip Reef Shark","Wildcat","Wildebeest","Wobbegong Shark","Wolf","Wolverine","Wombat","Woodchuck","Yak","Yellow-Bellied Marmot","Zebra","Zebu","Zorilla"]
        
tax_list = [["Common Name","Kingdom","Phylum","Class","Order","Family","Genus","Conservation Status"]]
        
for i in namelist:
       
    #Initializes the variables and refreshes them each loop
    con_status = "nan"
    kingdom = "nan"
    phylum = "nan"
    aclass = "nan"
    order = "nan"
    family = "nan"
    genus = "nan"
    
    #Gets page of the animal on wikipedia
    try:
        page = wikipedia.page(i)             
        
    except wikipedia.DisambiguationError:
        print("!!!Disambugation error for " + i)
        continue
    
    except wikipedia.PageError:
        print("!!!Page error for " + i)
        continue
    
    url = page.url   
    try:                                #Gets url of the page
        table = pd.read_html(url)[0]    #Gets the taxonomy table
    except ValueError:
        continue
    
    animal_list = table.values.tolist()
    
    try:
        if "This article" in str(animal_list[0][1]):
            table = pd.read_html(url)[1]
            animal_list = table.values.tolist()
            
            if "This article" in str(animal_list[0][1]):
                table = pd.read_html(url)[2]
                animal_list = table.values.tolist()
                
                if "This article" in str(animal_list[0][1]):
                    table = pd.read_html(url)[3]
                    animal_list = table.values.tolist()
                    
                    if "This article" in str(animal_list[0][1]):
                        table = pd.read_html(url)[4]
                        animal_list = table.values.tolist()
    except:
        continue
    
    #Name of the animal should be the title of the page
    animal_name = page.title                    
    
    #Performs search    
    for j in range(len(animal_list)):
        
        if "Conservation status" in str(animal_list[j][0]):
            con_status = animal_list[j+1][0]
        
        if "Kingdom:" in str(animal_list[j][0]):
            kingdom = animal_list[j][1]
        
        if "Phylum:" in str(animal_list[j][0]):
            phylum = animal_list[j][1]
            
        if "Class:" in str(animal_list[j][0]):
            aclass = animal_list[j][1]
        
        if "Order:" in str(animal_list[j][0]):
            order = animal_list[j][1]
        
        if "Family:" in str(animal_list[j][0]):
            family = animal_list [j][1]
            
        if "Genus:" in str(animal_list[j][0]):
            genus = animal_list [j][1]
    
    #Appends everything to temporary list, then adds that list to the main list
    tem = []
    tem.append(animal_name)
    tem.append(kingdom)
    tem.append(phylum)
    tem.append(aclass)
    tem.append(order)
    tem.append(family)
    tem.append(genus)
    tem.append(con_status)
    tax_list.append(tem)
    
    #Tells you how the script is progressing so you don't feel lonely
    print(i)
    
    #Sleeps after each search to not overwhelm the wikipedia server :)
    time.sleep(0.5)
    
#Writes everything into a pretty csv file    
with open('taxonomy_list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(tax_list)
