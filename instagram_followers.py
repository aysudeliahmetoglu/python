import instaloader

instagram = instaloader.Instaloader()
instagram.load_session_from_file("denemeaccount4")
accounts=["hsdyalova","hsdturkey","hsdgalata","hsdelazig","hsdgaun","hsdkaraman","hsdmef","hsdankara","hsddpu","hsdbtu","hsdokanuni","hsddenizli"]
i=0
while i < len(accounts):
  
    target_profile = instaloader.Profile.from_username(instagram.context,accounts[i])
    print(accounts[i]+ " takipci sayisi:", target_profile.followers)
    i+=1
