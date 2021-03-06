===========================================================

   Documentation for goodFor/badFor Corpus 

===========================================================

Contents:

  1. Introduction

  2. Annotation Scheme

     2.1 gfbf
     2.2 agent
     2.3 object
     2.4 influencer

  3. Data 

  4. Database Structure

     4.1 root folder/docs
     4.2 root folder/GATE
     4.3 root folder/MPQA

  5. MPQA Annotation Format

  6. Acknowledgement

  7. Contact Information

  8. References

-----------------------------------------------------------

1. Introduction

This corpus contains political editorials manually annotated
in GATE using an annotation scheme for events that
positively or negatively affect entities
(benefative/malefactive event) and for the attitude of the
writer toward the agents and objects of such events. For ease of
communication, we use the terms goodFor and badFor for benefactive
and malefactive events, respectively, and use the abbreviation
gfbf for an event that is one or the other.
 
Another component of the annotation is the influencer, a word
 whose effect is to either retain or reverse the polarity of 
a gfbf event. For example, in the sence below:

       "Tom didn't help Mary to deny the proposal."

In the gfbf event of "deny", "help" is a retainer while
"didn't" is a reverser.  

The annotation of the corpus was performed by 2 annotators,
one of the two wasn't involved in developing the annotation scheme.

At this time, the corpus is only available to researchers.

A description of this corpus is published in ACL 2013 short paper (Deng et al., 2013).

-----------------------------------------------------------

2. Annotation Scheme

This section contains an overview of the types of annotations 
that you will see marked in the documents of this corpus.  
The annotation scheme and agreement studies are described
in details in (Deng et al., 2013).  The complete annotation schema is
in the root folder.

2.1 goodFor/badFor

    Mark the text sapn of events that either positively affects objects
    (benefactive/goodFor events, such as help) or negatively affects
    objects (malefactive/badFor events, such as kill).

    Attributes:
        span - the text span expressing the gfbf event

        polarity - specifying the polarity of the gfbf
                   event

                   VALUES: goodFor, badFor 

        agentId - linking the agent of the gfbf event to it, by
                  specifying the id of the annotated agent span, etc
 
                  VALUES: id, implicit
           
                           Notice that if the agent is implicit, we do not
                           annotate an agent.For example, in the sentence:

                                    " The building was destoryed."

                           There is a gfbf event of "destroyed", but there
                           is no exlicit agent. 

        objectId - linking the object to the gfbf event to it, by 
                   specifying the id of the annotated object span, etc

                   VALUES: id
                           (a gfbf event always has an object)

2.2 agent

    Mark the text span referring to the agent of the gfbf
    event. For example, in the sentence below:

         "This policy decreases the healthcare cost."

    For the gfbf of "decreases", the agent is "This policy". 

    Attributes:
        span - the text span of the agent 

        writerAttitude - specifying the writer's attitude
                         towards the agent

                         VALUES: negative, positive, none 

2.3 object

    Mark the text span referring to the object of the gfbf
    event. For example, in the sentence mentioned above:

         "This policy decreases the healthcare cost."

    For the gfbf of "decreases", the object is "the
    healthcare cost". 

    Attributes:
        span - the text span of the object

        writerAttitude - specifying the writer's attitude
                         towards the object

                         VALUES: negative, positive, none

2.4 influencer

    Mark the text span which either retains or reversers the
    polarity of a gfbf event.

    Attibutes:
        span - the text span of influencer

        effect - specifying the function of the influencer
                 event

                   VALUES: retain, reverser

        agentId - linking the agent of the influencer to it,
                  by specifying the id of the annotated agent
                  span, etc

                  VALUES: id, implicit, or BLANK
                       
                       The criteria for annotating the agentId to be implicit
                       is consistent with that for the agent of a gfbf.
                       
                       There is one case where we could mark it as BLANK:
                       if the agent of a retainer is the same with the agent of its gfbf, 
                       we leave the agentId of the retainer to be BLANK.
  

        objectId - linking the object to the gfbf event to it, by
                   specifying the id of the annotated object span, etc

                   VALUES: id
                           (an influencer always has an object)

 
-----------------------------------------------------------

3. Data

The full corpus contains 134 documents, a total of 8,069 sentences.

The articles in the corpus are political editorials from blogs and
editorial about a controversial topic, "the Affordable Care Act".

In total, there are 1764 annotated gfbf triples, out of which 691 are
goodFor and 1073 are badFor. From the writer's perspective, 1662 noun
phrases are annotated positive, 1328 noun phrases are negative and the
remaining 8 are neutral, which are annotated as "none" or "unknown".

-----------------------------------------------------------

4. Database Structure

The folder contains three subdirectories: docs, GATE, MPQA and an annotation manual.

4.1 root folder/docs

    The docs subdirectory contains the original files of the corpus.  
    In this subdirectory, each file is named with the docId followed
    by the suffix of ".txt".

4.2 root folder/GATE
 
    The GATE subdirectory contains the annotated file in GATE.
    The output of each file is an XML file, generated by GATE. (For
    instructions about GATE and how to load the output in GATE, please
    refer to:http://mpqa.cs.pitt.edu/annotation/set_up_gate/ and http://mpqa.cs.pitt.edu/annotation/gate_basics/.) Each file is named with the docId, followed by the
    suffix of ".xml".

4.3 root folder/MPQA
   
    The file in MPQA subdirectory provides annotated output in MPQA format, as
    introduced later in Section 5. Each file is named with the docId,
    followed by the suffix of ".mpqa".

-----------------------------------------------------------

5. MPQA Annotation Format
(partially quoted from MPQA corpus developed by Wilson, http://mpqa.cs.pitt.edu/corpora/mpqa_corpus/)

The MPQA format is a type of generalstand-off annotation. Every line
in an annotation file is either a comment line (beginning with a '#")
or an annotation line (one annotation per line).

An MPQA annotation line consists of text fields separated by a
single TAB.  The fields used are listed below, with an example 
annotation underneath.

id	span	data_type	ann_type	attributes
3       334,340 string  	gfbfobject	polarity="positive" string="energy"

Every annotation has a identifier, id.  This id is unique ONLY 
within a given annotation file.

The span is the starting and ending byte of the annotation in 
the document. For example, the span of this annotation 
is 334,340.  This means that the start of this annotation is 
byte 334 in the raw file with corresponding doc id, and byte 340
is the character after the last character of the annotation.

     blah, blah, blah, example annotation, blah, blah, blah
                       |                 |
                  start byte          end byte

The data_type of all annotations should be 'string'.

The types of annotations are gfbf, gfbfagent, gfbfobject and
influencers. These annotation types correspond to the annotation
types described in Section 2.

An annotation may have any number of attributes. Multiple attributes
for an annotation are separated by single space, and they may be listed
in any order. The attributes that an annotation may have depends on
the type of annotation. The set of possible attributes for each
annotation type is listed in Section 2.

Note that the agent of an gfbf or influencer may be "implicit". In
that case the printing of "agent=" of the corresponding gfbf or
influencer is "implicit", instead of agentId. Moreover, we do not
print all "implicit" agents since they do not have any span in the
document.

-----------------------------------------------------------

6. Acknowledgements

This work was supported in part by DARPA-BAA-12-47 DEFT grant
#12475008 and National Science Foundation grant #IIS-0916046.

-----------------------------------------------------------

7. Contact Information

If you have any question about the annotation scheme, the corpus, or
you find annotations that you disagree, please contact Lingjia Deng at
the University of Pittsburgh. By all efforts can we have a better
corpus.

Lingjia Deng email: lid29@pitt.edu  -or-  lingjiadeng@gmail.com

-----------------------------------------------------------

8. References

Lingjia Deng, Janyce Wiebe, and Yoonjung Choi. 2013. Benefactive/Malefactive Event and Writer Attitude Annotation. In the 51st Annual Meeting of the Association for Computational Linguistics (ACL-2013, short paper). 

F.Zuniga and S.Kittila. 2010. Introduction. In F.Zuniga and S.Kittila,
editors, Benefatives and malefatives, Typological studies in language.
J.Benjamins Publishing Company.

Pranav Anand and Kevin Reschke. 2010. Verb classes as evaluativity
functor classes. In Interdisciplinary Workshop on Verbs. The
Identification and Representation of Verb Features.

Amit Goyal, Ellen Riloff, and Hal Daum III. 2012. A computational
model for plot units. Computational Intelligence, pages no-no.

Karo Moilanen and Stephen Pulman. 2007. Sentiment composition. In
Proceedings of RANLP 2007, Borovets, Bulgaria.

Alena Neviarouskaya, Helmut Prendinger, and Mitsuru Ishizuka. 2010.
Recognition of affect, judgment, and appreciation in text. In
Proceedings of the 23rd International Conference on Computational
Linguistics, COLING '10, pages 806-814, Stroudsburg, PA, USA.
Association for Computational Linguistics.

Alexander Conrad, Janyce Wiebe, Hwa, and Rebecca. 2012. Recognizing
arguing subjectivity and argument tags. In Proceedings of the Workshop
on Extra-Propositional Aspects of Meaning in Computational
Linguistics, ExProM '12, pages 80-88, Stroudsburg, PA, USA.
Association for Computational Linguistics.

Janyce Wiebe, Theresa Wilson, and Claire Cardie. 2005. Annotating
expressions of opinions and emotions in language. Language Resources
and Evaluation, 39(2/3):164-210.

-----------------------------------------------------------

Lingjia Deng
Janyce Wiebe
Yoonjung Choi

version 1.0  
last modified 1/16/14
