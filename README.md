**Team Mates:**
    1. 17MIS0133
    2. 17MIS0227
    3. 17MIS0299
    4. 17MIS0321
    5. 17MIS0333


The main objective of our project is to anlayse the Mood of the user based on his/her past data.

**Dataset :**
    Our own dataset (1 year music data) is collected from the official Spotify team by mailing.
    Also, we use Spotify API
   
**Features of the Tool :**
Our Tool is Python. As we all know Python is a general-purpose interpreted and high-level programming language. Since It supports various functional and structured programming modules we have chosen this tool to get high efficiency. 

**Why we Selelcted this tool :** 

**Advantages:**
Python provides many useful features which make it popular and valuable from the other programming languages. 
    * Python is easy to learn as compared to other programming languages. 
    * Due to the simplicity of Python (Syntax and behaviour), developers can focus on solving the problem.
    * Python can perform complex tasks using a few lines of code. 
    * The advantage of being interpreted language, it makes debugging easy and portable. 
    * Python is freely available for everyone and Python comes under the OSI approved open-source license.
    * It provides a vast range of libraries for the various fields such as machine learning, web developer, and also for the scripting. There are various machine learning libraries, such as Tensor flow, Pandas, Numpy, Keras, and Pytorch, etc. TensorFlow is an open-source library developed by Google primarily for deep learning applications. 
    * The code of the other programming language can use in the Python source code and vice versa.
    * Since Python forms the basis for new platforms like Raspberry Pi, it finds the future bright for the Internet Of Things.

**Disadvantages:**
    * The line by line execution of code often leads to slow execution. The dynamic nature of Python is also responsible for the slow speed of Python because it has to do the extra work while executing code.
    * To provide simplicity to the developer, Python has to do a little tradeoff. The Python programming language uses a large amount of memory. 
    * Python is generally used in server-side programming.Python is not memory efficient and it has slow processing power as compared to other languages so We don’t get to see Python on the client-side or mobile applications .
    * As we know Python is a dynamically typed language so the data type of a variable can change anytime. A variable containing integer number may hold a string in the future, which can lead to Runtime Errors.
    * As compared to the popular technologies like JDBC and ODBC, the Python’s database access layer is found to be bit underdeveloped and primitive. However, it cannot be applied in the enterprises that need smooth interaction of complex legacy data.

**Some Basic Concepts:**

*Libraries:* Python Libraries are a set of useful functions that eliminate the need for writing codes from scratch. We are going to several libraries in our project like Pandas, Numpy, Matplotand etc,. Numpy is considered as one of the most popular machine learning library in Python. 

*Dictionary :* We have dictionaries in python where keys are unique. We have so many different built-in functions and methods in the dictionaries. we can aslo access the values in the dictionary, update and delete the dictionary elements also. 

*Modules:* A module is same as a code library which contains a set of functions of our application. We can create our own module or simply we can import built-in modules using certain commands. For our project, we are using some built-in modules for operations like Math and OS module.

*JSON:* Since the spotify web API is made with javascript program. They also provide us the data as JSON file, JSON is text, written with JavaScript object notation. So we are going to change the format according to our needs.

*PANDA:* Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. Pandas can clean messy data sets, and make them readable and relevant.

1) The collected data was in the form of JSON file, then we used Py Panda module for converitng it to CSV file.

2) We are importing the Secure keys using .ENV (Environemental module) module which is provided by the official spotify team.

3) Spotify token authentication is nothing but validating the user with his/her profile link. We can read his/her profile but we can't change anything. This is done by Spotipy which is a lightweight Python library for the Spotify Web API. With Spotipy we get full access to all of the music data provided by the Spotify platform. We named it as SPOTANALYST.

4) By using the SPOTIFY API library, the Spotify Web API endpoints return JSON metadata about music artists, albums, and tracks, directly from the Spotify Data Catalogue. From that, we can get the required data for music analysis.

___

In Our project, the above steps are done till now. We are going to use 

**TOOLS:**

    - Spotify Library to get access to Spotify platform music data
    - Seaborn and matplotlib for data visualization (Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. 
    - Pandas and numpy for data analysis
    - Sklearn to build the Machine Learning model (Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms.) [from sklearn import datasets - for importing data and selecting the suitable ML algorithm]

**Spotify Audio Features:**

    Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
    Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
    Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. 
    Instrumentalness: Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. 
    Loudness: the overall loudness of a track in decibels (dB). 
    Tempo: The overall estimated tempo of a track in beats per minute (BPM) and so on.

    - Then we are going to visualize the data find corelation and relatioships between the attributes.

    - Then we are going to select the suitable ML algorithm and going to tune with Train the model for several echos to achieve great accuracy.

**Practical DEMO :**

1) After you have installed the library you need to get a client ID and client secretof Spotify in order to use their API. Go to the Dashboard for Spotify developers and login with your Spotify account.

2) 
# import matplotlib.pyplot as plt
# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",) 

3)we import them first
# import pandas as pd
creating a series and a DataFrame with different dtypes.we can perform various operations using appropriate commands.

4)scikit-learn comes with a few standard datasets.
from sklearn import datasets
Then Loading our datasets. Then choosing the paramaters of the model. Then we train the model. 	 