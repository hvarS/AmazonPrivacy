# NLP for PII Detection

We are using Presidio(Open Sourced - MSR) to detect the PII in the textual reviews that we obtain .

Before running the script , please run the following commands in your system :
> !pip install presidio-analyzer  
> !python -m spacy download en_core_web_lg

### Sample text I/O(for presidio) :
The entity to be detected in presidio is 'PHONE_NUM'  
**I/P** : My phone number is 212-555-5555  
**O/P** : [type: PHONE_NUMBER, start: 19, end: 31, score: 0.75]

This will ensure that presidio works perfectly with the existing text.

## TO DO with Presidio :
1. Find the useful Entities for our usecase PII Detection
2. Think of new entities that we can utilize for PII
3. Train the New Entities 
4. Test it on our scraped datasets 


