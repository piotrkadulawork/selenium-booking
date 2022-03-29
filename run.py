# 1:44:45
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.accept_cookies()
        bot.change_currency(currency='USD')
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2022-03-28',
                         check_out_date='2022-04-15')
        bot.select_adults(10)
        bot.click_search()
        bot.apply_filtration()

except Exception as e:
    if 'in PATH' in str(e):
        print("There is a problem running this program from command line")
    else:
        raise
