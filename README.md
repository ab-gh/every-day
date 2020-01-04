# every-day

## setup
1. generate a discord application with bot user, and save the Token ($TOKEN)

2. edit ln32 to:

`    user = await bot.fetch_user($YOUR_USER_ID)`

3. ssh into a vm

`$ git clone https://github.com/aejb/every-day`

`$ cd every-day`

`$ touch 2020.csv`

`$ echo $TOKEN >> token.txt`

4. crontab:

`$ crontab -e`

5. add:

`30 10 * * * python3.6 /home/$USR/every-day/bot.py`

6. profit
