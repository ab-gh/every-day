# every-day

## setup
generate a discord application with bot user, and save the Token ($TOKEN)
edit ln32 to:
`    user = await bot.fetch_user($YOUR_USER_ID)`
ssh into a vm
`$ git clone https://github.com/aejb/every-day`
`$ cd every-day`
`$ touch 2020.csv`
`$ echo $TOKEN >> token.txt`

crontab:
`$ crontab -e`

add:
`30 10 * * * python3.6 /home/$USR/every-day/bot.py`
