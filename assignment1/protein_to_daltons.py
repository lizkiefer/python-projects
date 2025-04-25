"""

File:  protein_to_daltons.py
Author: Liz Kiefer

Using a hardcoded protein sequence, calculate the average weight of the sequence in kilodaltons.
"""

PROTEIN_SEQUENCE = ("madpaagppp segeestvrf arkgalrqkn vhevknhkft arffkqptfc shctdfiwgf gkqgfqcqvc "
                   "cfvvhkrche fvtfscpgad kgpasddprs khkfkihtys sptfcdhcgs llyglihqgm kcdtcmmnvh "
                   "krcvmnvpsl cgtdhterrg riyiqahidr evlivvvrda knlvpmdpng lsdpyvklkl ipdpkseskq "
                   "ktktikcsln pewnetfrfq lkesdkdrrl sveiwdwdlt srndfmgsls fgiselqkag vdgwfkllsq "
                   "eegeyfnvpv ppegsegnee lrqkferaki gqgtkapeek tantiskfdn ngnrdrmklt dfnflmvlgk "
                   "gsfgkvmlse rkgtdelyav kilkkdvviq dddvectmve krvlalpgkp pfltqlhscf qtmdrlyfvm "
                   "eyvnggdlmy hiqqvgrfke phavfyaaei aiglfflqsk giiyrdlkld nvmldseghi kiadfgmcke "
                   "niwdgvttkt fcgtpdyiap eiiayqpygk svdwwafgvl lyemlagqap fegededelf qsimehnvay "
                   "pksmskeava ickglmtkhp gkrlgcgpeg erdikehaff ryidwekler keiqppykpk ardkrdtsnf "
                   "dkeftrqpve ltptdklfim nldqnefagf sytnpefvin v")

AMINO_ACIDS = len(PROTEIN_SEQUENCE.replace(' ', ''))
print('The length of "Protein kinase C beta type" is: ' + str(AMINO_ACIDS))

AVG_WEIGHT = 110
print('The average weight of this protein sequence in kilodaltons is: ' +
      str((AMINO_ACIDS * AVG_WEIGHT)/1000))
