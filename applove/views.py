from django.shortcuts import render, get_object_or_404 # this is a Django shortcut function, just like render is


###################################################
# VIEW
###################################################
def home(request):
    """ Shows a menu of views for the user to try """
    return (render(request, 'index.html'))


###################################################
# ERRORS: puts up a generic error page
###################################################
def errors(request):
    return (render(request, 'errors.html'))


########################################################
def about(request):
    return (render(request, 'about.html'))


########################################################
def blog(request):
    from .models import Post
    alltitles = Post.objects.values_list('title', flat=True).distinct()
    allbodies = Post.objects.values_list('body', flat=True).distinct()
    bodiestitles = zip(allbodies, alltitles)
    return render(request, 'blog.html', {'bodiestitles': bodiestitles})



########################################################
def contact(request):
    return (render(request, 'contact.html'))


########################################################
def menu(request):
    return (render(request, 'menu.html'))


####################################################
# Retrieves all the slugs from the table
####################################################
def show_the_post_slug(request):
    from .models import Post
    newstring=''
    postinfo = Post.objects.values_list('slug', flat=True).distinct()
    for instance in postinfo:
        newstring = instance + '<br>' + newstring
    return render(request, 'show_the_post_slug.html', {'postinfo': newstring})

####################################################
# Get the Title
####################################################
def show_the_post_titles(request):
    from .models import Post
    newstring=''
    postinfo = Post.objects.values_list('title', flat=True).distinct()  #<QuerySet ['How_I_Built_My_First_Django_Blog']>
    postbody=Post.objects.values_list('body', flat=True).distinct()
    for instance in postinfo:
        newstring = instance + '<br>' + newstring
    return render(request, 'show_the_post_titles.html', {'postinfo': newstring, 'postbody': postbody}) # How I Built My

####################################################
# Construct the Status
####################################################
def show_the_post_status(request):
    from .models import Post
    newstring=''
    postinfo = Post.objects.values_list('status', flat=True).distinct() # <QuerySet ['How_I_Built_My_First_Django_Blog']>
    for instance in postinfo:
        newstring=instance + '<br>' + newstring
    return render(request, 'show_the_post_status.html', {'postinfo': newstring}) # How I Built My First Django Blog


####################################################
def write_a_new_post(request):
    from django.contrib.auth.models import User
    from .models import Post
    user = User.objects.get(username='lindasuperuser')
    Post.objects.create(title='First post',
                             slug='First-post',
                             body='First stuff',
                             author=user)

    post = Post(title='Second post', slug='Second-post', body='Second Stuff', author=user)
    post.save()
    post = Post(title='Third post', slug='Third-post', body='Third Stuff', author=user)
    post.save() # Performs a SQL insert
    post = Post(title='Fourth post', slug='Fourth-post', body='Fourth Stuff', author=user)
    post.save()  # Performs a SQL insert
    return render(request, 'write_a_new_post.html')
####################################################
# Create a post, then change its title
####################################################
def change_the_title(request):

    from django.contrib.auth.models import User
    from .models import Post
    user = User.objects.get(username='lindasuperuser')

    post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
    post.save()

    post.title = 'New Title'
    post.save()

    return render(request, 'change_the_title.html')

####################################################
def retrieve_all_post_titles(request):

    from .models import Post
    newstring=''
    all_posts = Post.objects.all() #<QuerySet [<Post: One more post>, <Post: replaced title>, <Post: Fourth post>, <Post: Third post>, <Post: Second post>, <Post: First post>, <Post: How I Built My First Django Blog>, <Post: Start a new Django project in Pycharm>]>
    for instance in all_posts:
        newstring=str(instance) + '<br>' + newstring

    return render(request, 'retrieve_all_post_titles.html', {'all_posts':  newstring})
####################################################
def filter_the_posts(request):
    from django.contrib.auth.models import User
    from .models import Post
    newstring=''
    #objects is the default manager of every model. It retrieves everything from the database
    some_posts = Post.objects.filter(slug="Second-post")
    some_posts = Post.objects.filter(publish__year=2019)\
                             .exclude(title__startswith='Fourth')

    # filter choices are author, author_id, body, created, id, publish, slug, status, title, updated
    for instance in some_posts:
        newstring=str(instance) + '<br>' + newstring
    return render(request, 'filter_the_posts.html', {'some_posts': newstring})
####################################################
def order_post_alpha(request):
    from .models import Post
    newstring=''

    some_posts = Post.objects.order_by('title')
    some_posts = Post.objects.order_by('-title')
    for instance in some_posts:
        newstring=str(instance) + '<br>' + newstring
    return render(request, 'order_post_alpha.html', {'some_posts': newstring})
####################################################
# This view will work if there's one and only one of the startswith
def delete_a_post(request, titlestartswith='^'):
    from .models import Post
    #post = Post.objects.get(title__startswith='One') this works too
    post = get_object_or_404(Post, title__startswith="New Title")
    post.delete()
    return render(request, 'delete_a_post.html')

####################################################
# Display a Single Post So far, it shows status if I send in title
def display_a_single_post(request):
    from .models import Post
    post = Post.objects.get(title='Python Discoveries')
    # post = get_object_or_404(Post, slug=post,
    #                                status='published',
    #                                publish__year=year,
    #                                publish__month=month,
    #                                publish__day=day)
    return render(request,'display_a_single_post.html', {'post': post.status})



####################################################
# Show titles and full bodies
####################################################
def show_the_titles_and_bodies(request):
    from .models import Post
    alltitles = Post.objects.values_list('title', flat=True).distinct()
    allbodies = Post.objects.values_list('body', flat=True).distinct()
    bodiestitles=zip(allbodies,alltitles)
    return render(request, 'show_the_titles_and_bodies.html', {'bodiestitles': bodiestitles})
####################################################
# In the view I used Zip because you can't use zip in DTL
def show_the_post_bodies_truncated(request):
    from .models import Post
    alltitles = Post.objects.values_list('title', flat=True).distinct()
    allbodies = Post.objects.values_list('body', flat=True).distinct()
    bodiestitles=zip(allbodies,alltitles) # allows me to loop through two objects at the same time in the DTL
    return render(request, 'show_the_post_bodies_truncated.html', {'bodiestitles': bodiestitles})

###############################
#BLOGGERAPIGETCHRON retrieves the blog posts from blogger fullstacksafarie but does not save the blog posts in the model
###############################

  # Note: I had to lower the number of maxPosts above because the requests.get was throwing a server 500 error with too many posts. It
  # turns out that requests is much slower than urllib.request.urlopen. This is because
  # it doesn't use persistent connections: that is, it sends the header
  # "Connection: close". This forces the server to close the connection immediately, so that TCP FIN comes quickly. You can reproduce
  # this in Requests by sending that same header. Like this: r = requests.post(url=url, data=body, headers={'Connection':'close'})
  #
  # Note: I was able to improve the api call to fetchbodies = false, which speeds up the loading to some degree. Now I can allow for 200 posts
  # instead of 100 posts.
def bloggerapigetchron(request):
    def request_by_year(edate,sdate):
      # Initially I did the entire request at once, but I had to chunk it into years because it was timing out in windows.

      import json
      import requests
      # fullstackjourney id = 4018409536126807518
      url="https://www.googleapis.com/blogger/v3/blogs/4018409536126807518/posts?endDate=" + edate + "&fetchBodies=true&maxResults=64&startDate=" + sdate + "&status=live&view=READER&fields=items(title%2Curl%2Curl)&key=AIzaSyDleLQNXOzdCSTGhu5p6CPyBm92we3balg"

      r=requests.get(url, stream=True)
      q=json.loads(r.text)  # this is the better way to unstring it
      if not q:
         s= []
      else:
         s=q['items']
      return(s)

    accum_list=[]

    import datetime as d
    c_year = int(d.datetime.now().year)
    for the_year in range(2018, c_year+1):  # only works for 2019 to 2019 or 2019 to 2020

      enddate=str(the_year)+"-12-31T00%3A00%3A00-00%3A00"
      startdate=str(the_year)+"-01-01T00%3A00%3A00-00%3A00"
      t=request_by_year(enddate,startdate)
      accum_list=t+accum_list

    #from operator import itemgetter
    #sorteditems=sorted(accum_list,  key=itemgetter('title'), reverse=True)
    counter=0
    newstring=" "
    for mylink in accum_list:
        counter+=1
        newstring = "<a href="+ mylink['url'] + ">" + mylink['title'] + "</a>"  + "<br>" + newstring

    from django.contrib.auth.models import User
    from .models import Post
    user = User.objects.get(username='lindasuperuser')

    Post.objects.create(title='First post',
                        slug='First-post',
                        body='First stuff',
                        author=user)
    counter=0
    for myinfo in accum_list:
        counter+=1
        post = Post(title=myinfo['title'], slug=myinfo['url'],  author=user)
        #post.save()

    #post = Post(title='Third post', slug='Third-post', body='Third Stuff', author=user)
    #post.save()  # Performs a SQL insert
    #post = Post(title='Fourth post', slug='Fourth-post', body='Fourth Stuff', author=user)
    #post.save()  # Performs a SQL insert
    #return render(request, 'bloggerapigetchron.html', {'allofit': accum_list, 'count':counter})
    return render(request, 'bloggerapigetchron.html', {'allofit': newstring, 'count':counter})
###################################################
###############################
#BLOGGERAPIGETALL NEW! This is really just a function that, once finished, need only run once, as it pulls all current posts
# out of fullstacksafari blogger blog once and for all.
###############################
# This gets the chronological list of postids
def bloggerapigetall(request):
      import json
      import requests
      from fullstacksafari.utils import lmextractslug, lmextractcontent
      ##########################################################################
      # First get the list of post ids
      ##########################################################################
      url="https://www.googleapis.com/blogger/v3/blogs/4018409536126807518/posts?maxResults=500&fields=items%2Fid%2CnextPageToken&key=AIzaSyDleLQNXOzdCSTGhu5p6CPyBm92we3balg"
      r=requests.get(url, stream=True)
      q=json.loads(r.text)  # this is the better way to unstring it
      if not q:
         s= []
      else:
         s=q['items']
      list_of_post_ids = []
      for stuff in s:
          list_of_post_ids.append(stuff)
      ##########################################################################
      # Now run through the list of postids to get more info about each post
      ##########################################################################
      # This design uses just one loop to iterate through all of the post ids. At each iteration, it fetches what
      # it needs, and stuffs the info into the model.
      from django.contrib.auth.models import User
      from .models import Post
      user = User.objects.get(username='lindasuperuser')

      for onedict in list_of_post_ids:
          postid=onedict['id']
          url="https://www.googleapis.com/blogger/v3/blogs/4018409536126807518/posts/" + postid +"?fetchBody=true&fields=content%2Cpublished%2Ctitle%2Curl&key=AIzaSyDleLQNXOzdCSTGhu5p6CPyBm92we3balg"
          r = requests.get(url, stream=True)
          thedata=json.loads(r.text)

          post_title=thedata['title']
          post_content = lmextractcontent(thedata['content']) # This will remove the printfriendly code
          post_published=thedata['published']
          post_slug = lmextractslug(thedata['url'])  # This will extract the slug from the shole url
          # gather up all needed post data and add it to a record in the model
          post = Post(title=post_title, slug= post_slug, author=user,  body=post_content, publish=post_published)
          post.save()
      return render(request, 'bloggerapigetall.html', {'allofit':"Finished with Post Save"})

###################################################
###################################################
###################################################
###################################################
# Below are the Request Body and the Response for one of the posts
###################################################
"""
 
GET https://www.googleapis.com/blogger/v3/blogs/4018409536126807518/posts/4487191146444331910?fetchBody=true&fields = content%2Cpublished%2Ctitle%2Curl&key = {YOUR_API_KEY}

Response

200
OK

- Show
headers -

{
    "published": "2019-02-24T04:23:00-08:00",
    "url": "http://fullstacksafari.blogspot.com/2019/02/django-trivia.html",
    "title": "Django This and That",
    "content": "<script>var pfHeaderImgUrl = '';var pfHeaderTagline = '';var pfdisableClickToDel = 0;var pfHideImages = 0;var pfImageDisplayStyle = 'right';var pfDisablePDF = 0;var pfDisableEmail = 0;var pfDisablePrint = 0;var pfCustomCSS = '';var pfBtVersion='2';(function(){var js,pf;pf=document.createElement('script');pf.type='text/javascript';pf.src='//cdn.printfriendly.com/printfriendly.js';document.getElementsByTagName('head')[0].appendChild(pf)})();</script><a class=\"printfriendly\" href=\"https://www.printfriendly.com/\" onclick=\"window.print();return false;\" style=\"color: #6d9f00; text-decoration: none;\" title=\"Printer Friendly and PDF\"><img alt=\"Print Friendly and PDF\" src=\"https://2.bp.blogspot.com/-_pA-Rf25q-g/Wz4GCdLo6XI/AAAAAAAAVKQ/PsFbM1HrvXofTuC0WbLFJ6Q4be1h2Y1HwCLcBGAs/s1600/printfriendly-button-md%2Bfinished%2Bwith%2Btan.jpg\" style=\"-webkit-box-shadow: none; border: none; box-shadow: none;\" /></a>\n\n<br />\n<ol>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">'' and '^' mean the same thing&nbsp;</span></li>\n<span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">\n</span>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">Django comes with a default API for doing CRUD. It's called the ORM</span></li>\n<span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">\n</span>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">The ORM is compatible with MySQL, PostgreSQL, SQLite, and Oracle</span></li>\n<span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">\n</span>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">Here is the documentation for the <a href=\"https://docs.djangoproject.com/en/2.2/ref/models/\">ORM</a></span> </li>\n<span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">\n</span>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">0001_initial.py is what's produced by makemigrations</span></li>\n<span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">\n</span>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">Synching the database: python manage.py migrate</span></li>\n<span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">\n</span>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">Objects is the default manager of every model. It retrieves all objects in the database</span></li>\n<li><span style=\"font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;\">Functions that you want to share across views shouldn't go into a view; instead they should go into utils.py <span style=\"background-color: white; color: #242729; display: inline; float: none; font-size: 15px; font-style: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px;\">and then import it and use it from the application files that need it. Coders disagree as to best place to put it. (Choice between in the root, or in the app).</span></span> </li>\n</ol>\n<ol>\n</ol>\n<h2>\n</h2>\n<h2>\nI belong to a private, fee-based group of Pythonistas. </h2>\nIf you would like to know more about <a href=\"https://www.pythonistacafe.com/\">PythonistaCafe</a>, where we share thoughts, ideas, fixes, and a sense of courteous community, look to <a href=\"https://dbader.org/\" target=\"_blank\">Dan Bader</a>, who started it all. He also offers free tips by email.\n\nOh, and if you take an interest in good marketing writing, read his stuff for that reason too.&nbsp; \n"
}

 

"""