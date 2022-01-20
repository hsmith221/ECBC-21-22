# Directory of Files and Description of Each File

## [Lexicons:](https://docs.google.com/document/d/1G0PKAmOIRlD1yn4uk1YR68UuProNAem7p7h_IjFVbN0/edit)
- *Economic:* economic related terms relevant to broader research
- *Legal:* law related terms relevant to broader research
- *Medical:* medicine related terms relevant to broader research
- *Metaphorical:* interesting metaphorical language
- *Political:* politics related terms relevant to broader research

## Monopoly Topic Modeling
- *eic_lexicons.ipynb*: Copying files from monopoly_eebo that mention the East India Company to a local folder called eic_monopoly_eebo. Finding the frequencies of target words from our lexicon within these files to get the raw input for word cloud generators. Also includes the code for Named Entity Recognition on eic_monopoly_eebo texts. 
- *eic titles and filenames.txt:* List of Restoration-era texts which mention both monopoly and EIC. 
- *eic_monopoly_TFIDF.ipynb*: Finding term frequency - inverse document frequency of texts within eic_monopoly_eebo 
- *Filter_All_Texts*: Function for filtering all EEBO cleaned files for a desired term.
- *filtering_eebo_restoration_monopoly.ipynb:* Filtering through all clean EEBO CSV files to write out texts from 1660-1714 into a separate local folder. From the folder of era-specific CSV files, write out a copy of ones which mention monopoly into a local folder called monopoly_eebo. 
- *Images*: Folder with visualizations from the files above 
- *monopoly_frequency.ipynb*: Finding and sorting the term frequency of "monopoly" within each file of the monopoly_eebo folder. 
- *patterns_eebo.ipynb*: Making scatterplots for the occurrences of certain words within all of EEBO. 
- *sortedMonopolyFrequency.txt:* Texts in monopoly_eebo sorted by the frequencies of "monopoly"
- *sortedNamedEntityRecognition.txt*: Sorted output from NER. 
- *Stopword_Additions*: Lexicon of stopwords our group finds relevant to remove from word-count based analyis.
- *tfidf.ipynb*: R code for generating visualizations of the top TF-IDF words in each file of eic_monopoly_eebo
- *Topic_Model_Attempt_1.ipynb:* First attempt at LDA based topic modeling on EIC texts.
- *Word_Cloud.ipynb:* This file comprises a function which creates a word cloud out of the text columns of a csv file. It has been run on the texts containing monopoly and East India Company.

## Update as added
