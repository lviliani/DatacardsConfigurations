#
# VH 2011 cut based   SF
#


tag='vh_cutBased'

lumi=4.922
chans=['sf_vh2j']

mcset='vh_sf'
dataset='Data2011'

energy='7TeV'

#variable='mll' # remember, y:x
variable='1' # remember, y:x
selection='vh2011'

range = (1,0,2)

xlabel='events'

# rebin=10
rebin=1


# directories
path_latino = '/data2/amassiro/VBF/Summer12/28Jan2013/Shape/tree_42x_skim_wwmin/'
path_dd     = '/data2/amassiro/VBF/Summer12/28Jan2013/Shape/dd/Cut_2011_5fb/'



# other directories
path_shape_raw='raw'
path_shape_merged='merged'



shapeFlags = [('CMS_7TeV_ch_res',False),('CMS_7TeV_hww_WJet_FakeRate_m_shape_2j',False),('CMS_7TeV_hww_WJet_FakeRate_e_shape_2j',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]

skipSyst = ['chargeResolution','puW_up','puW_down']
