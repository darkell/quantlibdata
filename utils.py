import json


def t_write_results(file_name, results):
    file = open("target/" + file_name, "w")
    file.write(json.dumps(results, indent=2))
    file.close()


def t_date_to_string(date):
    return str(date.year()) + "-" + str(date.month()).zfill(2) + "-" + str(date.dayOfMonth()).zfill(2)


def t_to_compounding(i):
    if i == 0:
        return "Simple"
    elif i == 1:
        return "Compounded"
    elif i == 2:
        return "Continuous"
    elif i == 3:
        return "SimpleThenCompounded"
    else:
        return ""


def t_to_frequency(frequency):
    if frequency == -1:
        return "NoFrequency"
    elif frequency == 0:
        return "Once"
    elif frequency == 1:
        return "Annual"
    elif frequency == 2:
        return "Semiannual"
    elif frequency == 3:
        return "EveryFourthMonth"
    elif frequency == 4:
        return "Quarterly"
    elif frequency == 6:
        return "Bimonthly"
    elif frequency == 12:
        return "Monthly"
    elif frequency == 13:
        return "EveryFourthWeek"
    elif frequency == 26:
        return "Biweekly"
    elif frequency == 52:
        return "Weekly"
    elif frequency == 365:
        return "Daily"
    elif frequency == 999:
        return "OtherFrequency"
    else:
        return "Unknown " + str(frequency)


def t_to_day_counter(day_counter):
    if day_counter.name() == "Actual/365 (Fixed)":
        return {"@type": "Actual365Fixed"}
    elif day_counter.name() == "Actual/Actual (ISDA)":
        return {"@type": "ActualISDA"}
    elif day_counter.name() == "Actual/Actual (AFB)":
        return {"@type": "ActualAFB"}
    elif day_counter.name() == "30/360 (Bond Basis)":
        return {"@type": "Thirty360BondBasis"}
    elif day_counter.name() == "30E/360 (Eurobond Basis)":
        return {"@type": "Thirty360EurobondBasis"}
    elif day_counter.name() == "30/360 (Italian)":
        return {"@type": "Thirty360Italian"}
    else:
        return "Unknown" + day_counter.name()


def t_to_calendar(calendar):
    if calendar.name() == "TARGET":
        return {"@type": "Target"}
    elif calendar.name() == "US settlement":
        return {"@type": "UnitedStatesSettlement"}
    else:
        return {"@type": calendar.name()}


def t_to_businessDayConvention(businessDayConvention):
    if businessDayConvention == 0:
        return "Following"
    elif businessDayConvention == 1:
        return "ModifiedFollowing"
    elif businessDayConvention == 2:
        return "Preceding"
    elif businessDayConvention == 3:
        return "ModifiedPreceding"
    elif businessDayConvention == 4:
        return "Unadjusted"
    elif businessDayConvention == 5:
        return "HalfMonthModifiedFollowing"
    elif businessDayConvention == 6:
        return "Nearest"
    else:
        return "Unknown " + str(businessDayConvention)

def t_time_unit(time_unit):
    if time_unit == 0:
        return "DAYS"
    elif time_unit == 1:
        return "WEEKS"
    elif time_unit == 2:
        return "MONTHS"
    elif time_unit == 3:
        return "YEARS"
    else:
        return "Unknown " + str(time_unit)


def t_interest_rate(interest_rate):
    return {
        "rate": interest_rate.rate(),
        "dayCounter": t_to_day_counter(interest_rate.dayCounter()),
        "compounding": t_to_compounding(interest_rate.compounding()),
        "frequency": t_to_frequency(interest_rate.frequency())
    }


def t_flat_forward(reference_date, day_counter, simple_quote_value, compounding, frequency):
    return {
        "referenceDate": t_date_to_string(reference_date),
        "dayCounter": t_to_day_counter(day_counter),
        "forward": {
            "@type": "SimpleQuote",
            "value": simple_quote_value
        },
        "compounding": t_to_compounding(compounding),
        "frequency": t_to_frequency(frequency)
    }

