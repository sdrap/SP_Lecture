
import fastbox as fb

fb.login('lyq', [PLEASE CHANGE IT TO YOUR PASSWORD])
# PORTFOLIO_ID = '42'
port = fb.PortfolioAPI(portfolio_id='42')
    
port.init(name="新策略", from_date="2021-01-01", to_date="2021-12-31", initial_cash=1000000, model="FactorCAPM", params={"factors": ["factor1", "factor2", "factor3"]})
# ----------
# you can do some thing here
port.command(None, pal="8")
# ----------
port.submit()
    