from setuptools import find_packages , setup 





setup( 
    name="crop-recommendation" , 
    version='0.0.0.1' , 
    author = "Rohit Katkar" , 
    author_email= "katkarrohit203@gmail.com" , 
    packages=find_packages() ,
    description="A package for recommending crops based on soil and environmental features.",
    license="MIT", 
    keywords="crop recommendation agriculture machine learning"


)