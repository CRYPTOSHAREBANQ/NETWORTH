from django.shortcuts import render
from .models import Account, UserAssets
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def estate_net_worth(request):

    if request.method == "GET":
        user_data = Account.objects.get(user=request.user)

        context = {
            "net_worth": user_data.net_worth
        }

        return render(request, 'estate_net_worth.html', context)


    return render(request, 'estate_net_worth.html')

@login_required
def edit_estate_net_worth(request):
    def update_asset(asset_id, asset_name, asset_worth, asset_extrafield = None):
        asset = UserAssets.objects.get(pk=asset_id)
        asset.name = asset_name
        asset.worth = asset_worth

        if asset_extrafield is not None:
            asset.extra_field = asset_extrafield
        
        asset.save()

    if request.method == "GET":

        bank = UserAssets.objects.filter(email=request.user, type="BANK")
        real_estate = UserAssets.objects.filter(email=request.user, type="REAL_ESTATE")
        insurance = UserAssets.objects.filter(email=request.user, type="INSURANCE")
        cryptocurrency = UserAssets.objects.filter(email=request.user, type="CRYPTOCURRENCY")
        nft = UserAssets.objects.filter(email=request.user, type="NFT")
        stock = UserAssets.objects.filter(email=request.user, type="STOCK")
        startup = UserAssets.objects.filter(email=request.user, type="STARTUP_INVESTMENT")
        jewelry = UserAssets.objects.filter(email=request.user, type="JEWELRY")
        car = UserAssets.objects.filter(email=request.user, type="CAR")
        #net worth information
        user_data = Account.objects.get(user=request.user)

        context = {
            "banks": bank,
            "real_estates": real_estate,
            "insurances": insurance,
            "cryptocurrencies": cryptocurrency,
            "nfts": nft,
            "stocks": stock,
            "startups": startup,
            "jewelries": jewelry,
            "cars": car,
            "currencies":FIAT_CURRENCIES,
            "net_worth": user_data.net_worth
        }

        return render(request, 'estate_net_worth_edit.html', context)        

    bank_ids = request.POST.getlist("asset_bank_id")
    bank_names = request.POST.getlist("asset_bank", None)
    bank_worths = request.POST.getlist("asset_bank-worth", None)

    real_estate_ids = request.POST.getlist("asset_real_estate_id")
    real_estate_names = request.POST.getlist("asset_real-estate", None)
    real_estate_worths = request.POST.getlist("asset_real-estate-worth", None)

    insurance_ids = request.POST.getlist("asset_insurance_id")
    insurance_names = request.POST.getlist("asset_insurance", None)
    insurance_worths = request.POST.getlist("asset_insurance-worth", None)

    cryptocurrency_ids = request.POST.getlist("asset_cryptocurrency_id")
    cryptocurrency_names = request.POST.getlist("asset_cryptocurrency", None)
    cryptocurrency_worths = request.POST.getlist("asset_cryptocurrency-worth", None)

    nft_ids = request.POST.getlist("asset_nft_id")
    nft_names = request.POST.getlist("asset_nft", None)
    nft_worths = request.POST.getlist("asset_nft-worth", None)

    stock_ids = request.POST.getlist("asset_stock_id")
    stock_names = request.POST.getlist("asset_stock", None)
    stock_worths = request.POST.getlist("asset_stock-worth", None)
    stock_extrafield = request.POST.getlist("asset_stock-extradata", None)

    startup_ids = request.POST.getlist("asset_startup_id")
    startup_names = request.POST.getlist("asset_startup", None)
    startup_worths = request.POST.getlist("asset_startup-worth", None)
    startup_extrafield = request.POST.getlist("asset_startup-extradata", None)

    jewelry_ids = request.POST.getlist("asset_jewelry_id")
    jewelry_names = request.POST.getlist("asset_jewelry", None)
    jewelry_worths = request.POST.getlist("asset_jewelry-worth", None)

    car_ids = request.POST.getlist("asset_car_id")
    car_names = request.POST.getlist("asset_car", None)
    car_worths = request.POST.getlist("asset_car-worth", None)
    car_extrafield = request.POST.getlist("asset_car-extradata", None)

    net_worth = 0

    for index, item in enumerate(bank_ids):
        if not bank_names[index] or not bank_worths[index]:
            continue

        asset_type = "BANK"
        if item:
            update_asset(item, bank_names[index], bank_worths[index])
        else:
            asset_bank = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=bank_names[index],
                worth=bank_worths[index]
            )
    
        net_worth += float(bank_worths[index])
    
    for index, item in enumerate(real_estate_ids):
        if not real_estate_names[index] or not real_estate_worths[index]:
            continue

        asset_type = "REAL_ESTATE"
        if item:
            update_asset(item, real_estate_names[index], real_estate_worths[index])
        else:
            asset_real_estate = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=real_estate_names[index],
                worth=real_estate_worths[index]
            )
        
        net_worth += float(real_estate_worths[index])
    
    for index, item in enumerate(insurance_ids):
        if not insurance_names[index] or not insurance_worths[index]:
            continue

        asset_type = "INSURANCE"
        if item:
            update_asset(item, insurance_names[index], insurance_worths[index])
        else:
            asset_insurance = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=insurance_names[index],
                worth=insurance_worths[index]
            )

        net_worth += float(insurance_worths[index])
    
    for index, item in enumerate(cryptocurrency_ids):
        if not cryptocurrency_names[index] or not cryptocurrency_worths[index]:
            continue

        asset_type = "CRYPTOCURRENCY"
        if item:
            update_asset(item, cryptocurrency_names[index], cryptocurrency_worths[index])
        else:
            asset_cryptocurrency = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=cryptocurrency_names[index],
                worth=cryptocurrency_worths[index]
            )

        net_worth += float(cryptocurrency_worths[index])
    
    for index, item in enumerate(nft_ids):
        if not nft_names[index] or not nft_worths[index]:
            continue

        asset_type = "NFT"
        if item:
            update_asset(item, nft_names[index], nft_worths[index])
        else:
            asset_nft = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=nft_names[index],
                worth=nft_worths[index]
            )

        net_worth += float(nft_worths[index])
    
    for index, item in enumerate(stock_ids):
        if not stock_names[index] or not stock_worths[index]:
            continue

        asset_type = "STOCK"
        if item:
            update_asset(item, stock_names[index], stock_worths[index], stock_extrafield[index])
        else:
            asset_stock = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=stock_names[index],
                worth=stock_worths[index],
                extra_field=stock_extrafield[index]
            )

        net_worth += float(stock_worths[index])
    
    for index, item in enumerate(startup_ids):
        if not startup_names[index] or not startup_worths[index]:
            continue

        asset_type = "STARTUP_INVESTMENT"
        if item:
            update_asset(item, startup_names[index], startup_worths[index], startup_extrafield[index])
        else:
            asset_startup = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=startup_names[index],
                worth=startup_worths[index],
                extra_field=startup_extrafield[index]
            )

        net_worth += float(startup_worths[index])

    for index, item in enumerate(jewelry_ids):
        if not jewelry_names[index] or not jewelry_worths[index]:
            continue

        asset_type = "JEWELRY"
        if item:
            update_asset(item, jewelry_names[index], jewelry_worths[index])
        else:
            asset_jewelry = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=jewelry_names[index],
                worth=jewelry_worths[index]
            )

        net_worth += float(jewelry_worths[index])
    
    for index, item in enumerate(car_ids):
        if not car_names[index] or not car_worths[index]:
            continue

        asset_type = "CAR"
        if item:
            update_asset(item, car_names[index], car_worths[index], car_extrafield[index])
        else:
            asset_car = UserAssets.objects.create(
                email=request.user,
                type=asset_type,
                name=car_names[index],
                worth=car_worths[index],
                extra_field=car_extrafield[index]
            )

        net_worth += float(car_worths[index])

    account = Account.objects.get(user=request.user)
    account.net_worth = net_worth
    account.save()

    return redirect('atm_functions:EditEstateNetWorth')