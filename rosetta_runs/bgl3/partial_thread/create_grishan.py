
# coding: utf-8

# In[41]:

import screed


# In[50]:

grishin_format = '''
## not_used {template_name}_thread
#
scores_from_program: 0
0 {target_sequence}
0 {template_sequence}
--
'''


# In[54]:

for i, record in enumerate( screed.open( 'run_A/partial_thread/aligned.fa' ) ):
    if i == 0:
        target_sequence = record.sequence
        target_name = record.name
    else:
        print( grishin_format.format( template_name=record.name, target_sequence=target_sequence, template_sequence=record.sequence ) )


# In[ ]:



