from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import json
import http.client
from datetime import datetime
import requests
from collections import Counter
import urllib.request, json
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
# VIEWS FOR FILTER APP
ignore_words = ["a","able","about","above","abroad","according","accordingly","across","actually","adj","after","afterwards","again","against","ago","ahead","aint","all","allow","allows","almost","alone","along","alongside","already","also","although","always","am","amid","amidst","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","arent","around","as","as","aside","ask","asking","associated","at","available","away","awfully","b","back","backward","backwards","be","became","because","become","becomes","becoming","been","before","beforehand","begin","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","came","can","cannot","cant","cant","caption","cause","causes","certain","certainly","changes","clearly","cmon","co","co.","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldnt","course","cs","currently","d","dare","darent","definitely","described","despite","did","didnt","different","directly","do","does","doesnt","doing","done","dont","down","downwards","during","e","each","edu","eg","eight","eighty","either","else","elsewhere","end","ending","enough","entirely","especially","et","etc","even","ever","evermore","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","fairly","far","farther","few","fewer","fifth","first","five","followed","following","follows","for","forever","former","formerly","forth","forward","found","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadnt","half","happens","hardly","has","hasnt","have","havent","having","he","hed","hell","hello","help","hence","her","here","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","him","himself","his","hither","hopefully","how","howbeit","however","hundred","i","id","ie","if","ignored","ill","im","immediate","in","inasmuch","inc","inc.","indeed","indicate","indicated","indicates","inner","inside","insofar","instead","into","inward","is","isnt","it","itd","itll","its","its","itself","ive","j","just","k","keep","keeps","kept","know","known","knows","l","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","likewise","little","look","looking","looks","low","lower","ltd","m","made","mainly","make","makes","many","may","maybe","maynt","me","mean","meantime","meanwhile","merely","might","mightnt","mine","minus","miss","more","moreover","most","mostly","mr","mrs","much","must","mustnt","my","myself","n","name","namely","nd","near","nearly","necessary","need","neednt","needs","neither","never","neverf","neverless","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","noone","nor","normally","not","nothing","notwithstanding","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","ones","only","onto","opposite","or","other","others","otherwise","ought","oughtnt","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","past","per","perhaps","placed","please","plus","possible","presumably","probably","provided","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","recent","recently","regarding","regardless","regards","relatively","respectively","right","round","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","shant","she","shed","shell","shes","should","shouldnt","since","six","so","some","somebody","someday","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","thatll","thats","thats","thatve","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","thered","therefore","therein","therell","therere","theres","theres","thereupon","thereve","these","they","theyd","theyll","theyre","theyve","thing","things","think","third","thirty","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","till","to","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","under","underneath","undoing","unfortunately","unless","unlike","unlikely","until","unto","up","upon","upwards","us","use","used","useful","uses","using","usually","v","value","various","versus","very","via","viz","vs","w","want","wants","was","wasnt","way","we","wed","welcome","well","well","went","were","were","werent","weve","what","whatever","whatll","whats","whatve","when","whence","whenever","where","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","whichever","while","whilst","whither","who","whod","whoever","whole","wholl","whom","whomever","whos","whose","why","will","willing","wish","with","within","without","wonder","wont","would","wouldnt","x","y","yes","yet","you","youd","youll","your","youre","yours","yourselves","yourself","youve","z","zero", "a", "an", "the", "is", "of", "are", "to", "in", "and", "as", "that", "from","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

@xframe_options_exempt
def index(request):
    context = {
        'keywords': Keyword.objects.order_by("-created_at"),
        'logged_in': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "filter/index.html", context)

def get_wordcount_from_API(input_response):
    sample = input_response.json()
    results = []
    for item in sample['results']:
        if 'title' in item:
            title = item['title'].lower()
            original_title = item['original_title'].lower()
        elif 'name' in item:
            title = item['name'].lower()
            if 'original_name' in item:
                original_title = item['original_name'].lower()
            else:
                original_title = item['name'].lower()
        if 'overview' in item:
            overview = item['overview'].lower()
        for char in "-.,\n:;\'":
            title = title.replace(char, '')
            original_title = original_title.replace(char, '')
            if 'overview' in item:
                overview = overview.replace(char, '')
        for word in title.split():
            if word not in ignore_words:
                results.append(word)
        for word in original_title.split():
            if word not in ignore_words:
                results.append(word)
        for word in overview.split():
            if word not in ignore_words:
                results.append(word)
    sorted_results = Counter(results).most_common()
    my_list_str = ""
    for item in sorted_results:
        if my_list_str.count(",") <= 20:
            if item[0].isalpha():
                my_list_str += item[0] + ", "
    print(my_list_str)
    return my_list_str

@xframe_options_exempt
def dic_json(request):
    my_list = Keyword.objects.last().query_data
    print(my_list)
    my_lst = my_list.split(",")
    print(my_lst)
    responseData = {
        'master_list' : my_lst
    }
    return JsonResponse(responseData)

def create_filter(request):
    if request.method == "POST":
        errors = Keyword.objects.keyword_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/filter/display_create_filter")
        else:
            title_to_filter = request.POST['title_to_filter']
            genre_to_filter = request.POST['genre_to_filter']
            payload = {
                'title_to_filter': title_to_filter,
                'genre_to_filter': genre_to_filter,
            }
            title_query = get_wordcount_from_API(requests.get(f"https://api.themoviedb.org/3/search/multi?api_key=5777e36919401c47664693585a0c8d92&query={payload['title_to_filter']}"))
            genre_query = get_wordcount_from_API(requests.get(f"https://api.themoviedb.org/3/search/multi?api_key=5777e36919401c47664693585a0c8d92&query={payload['genre_to_filter']}"))
            user = User.objects.get(id=request.session['user_id'])
            new_keyword = Keyword.objects.create(
                title_to_filter = request.POST['title_to_filter'],
                genre_to_filter = request.POST['genre_to_filter'],
                filter_end_date = request.POST['filter_end_date'],
                user_id = user,
                query_data = title_query
            )
            return redirect("/filter")

@xframe_options_exempt
def display_create_filter(request):
    return render(request, "filter/filtered_page.html")

@xframe_options_exempt
def delete_filter(request, id):
    dead_filter = Keyword.objects.get(id = id)
    dead_filter.delete()
    return redirect("/filter")

# def auto_delete_filter(request):
#     Keyword.objects.get()
#     today = datetime.now()
#     filter_end_date = request.POST['filter_end_date']
#     if today >= str(filter_end_date):



