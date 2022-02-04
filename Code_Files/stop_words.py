from gensim.utils import simple_preprocess
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words.extend(['thus', 'thereof', 'thence', 'thee', 'therein', 
                    'wherein', 'whereby', 'whereas', 'also', 'us', 'upon', 
                    'would', 'within', 'indeed', 'become', 'viz', 'per', 'anno', 
                    'whilst', 'thoe', 'ome', 'uch', 'said', 'shall', 'hath',
                    'may','made','much','one','mr','how','like','full','one',
                    'two','three','four','five','day','say','thou','make',
                    'done','do','have','well','know','heard','hear',
                    'saying','come','never','time','think','came','till','might',
                    'could','begin','began','took','went','last','matter','seeing',
                    'go','many','few','see','take','found','without','little','long',
                    'put','brought','bring','another','th','aforesaid','old',
                    'tell','em','yet','cae','mot','doe','aloe','every','elf',
                    'himelf','thy','de','ch','com','says','part','through','let',
                    'must','sir','tho','away','part','unto','printed','doth',
                    'iq','esq','firt','et','among','everal','ver','called','lt',
                    'every','even','becaue','ibid','de','lib','ch','com','often',
                    'againt','second','dr','though','goes','non','equire',
                    'page','told','hold','sr','ditto','elf','therefore','de',
                    'ps','six','ent','mr','inits','ee','ay','mut','almost',
                    'concerning','ey','vol','near','since','always'])
        
def remove_stopwords(data):
    return [[word for word in simple_preprocess(str(doc))
            if word not in stop_words] for doc in data]