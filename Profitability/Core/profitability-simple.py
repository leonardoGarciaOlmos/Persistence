class ProfitabilitySimple():

    def Calculate_Profitability_Simple(self, valueEnd, valueBegin):
        retProfitability = ((valueEnd - valueBegin) / valueBegin) * 100
        return retProfitability
        