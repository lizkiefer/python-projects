pro_seq = ("madpaagppp segeestvrf arkgalrqkn vhevknhkft arffkqptfc shctdfiwgf gkqgfqcqvc "
                   "cfvvhkrche fvtfscpgad kgpasddprs khkfkihtys sptfcdhcgs llyglihqgm kcdtcmmnvh "
                   "krcvmnvpsl cgtdhterrg riyiqahidr evlivvvrda knlvpmdpng lsdpyvklkl ipdpkseskq "
                   "ktktikcsln pewnetfrfq lkesdkdrrl sveiwdwdlt srndfmgsls fgiselqkag vdgwfkllsq "
                   "eegeyfnvpv ppegsegnee lrqkferaki gqgtkapeek tantiskfdn ngnrdrmklt dfnflmvlgk "
                   "gsfgkvmlse rkgtdelyav kilkkdvviq dddvectmve krvlalpgkp pfltqlhscf qtmdrlyfvm "
                   "eyvnggdlmy hiqqvgrfke phavfyaaei aiglfflqsk giiyrdlkld nvmldseghi kiadfgmcke "
                   "niwdgvttkt fcgtpdyiap eiiayqpygk svdwwafgvl lyemlagqap fegededelf qsimehnvay "
                   "pksmskeava ickglmtkhp gkrlgcgpeg erdikehaff ryidwekler keiqppykpk ardkrdtsnf "
                   "dkeftrqpve ltptdklfim nldqnefagf sytnpefvin v")

protein_sequence = len(pro_seq.replace(' ', ''))
print('The length of "Protein kinase C beta type" is: ' + str(protein_sequence))


molecular_weight = 110
average_mol_weight = (protein_sequence * molecular_weight)/1000
print('The average weight of this protein sequence in kilodaltons is: ' + str(average_mol_weight))



