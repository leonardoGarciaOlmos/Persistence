class ProfitabilitySimple():

    def Calculate_Profitability_Simple(self, valueEnd, valueBegin):
        
        if(type(valueEnd) != float or type(valueBegin) != float):
            return None

        if(valueEnd == 0.0 and valueBegin == 0.0):
            return None

        retProfitability = ((valueEnd - valueBegin) / valueBegin) * 100.00
        
        return float("{:.4f}".format(retProfitability))
        