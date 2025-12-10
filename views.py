from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product

def add_to_cart(request, product_id):
    print(f"DEBUG: add_to_cart called for product_id: {product_id}")
    cart = request.session.get('cart', {})
    print(f"DEBUG: Cart before adding: {cart}")

    if str(product_id) in cart:
        # در اینجا باید مقدار رو به جای 1، به مقدار قبلی اضافه کنی
        # اگر میخواهی هر بار 1 دونه اضافه بشه، کد فعلی درسته.
        # اگر می‌خواهی تعداد رو از جایی بگیری، باید اینجا تغییر بدی.
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    print(f"DEBUG: Cart after adding and saving to session: {request.session.get('cart')}")
    # مهم: این خط زیر رو اضافه کن تا مطمئن بشیم سشن ذخیره میشه
    request.session.modified = True 
    print(f"DEBUG: Redirecting to cart:cart_detail after adding product {product_id}")
    return redirect('cart:cart_detail') # <-- اصلاح شده اینجا

def remove_from_cart(request, product_id):
    print(f"DEBUG: remove_from_cart called for product_id: {product_id}")
    cart = request.session.get('cart', {})
    print(f"DEBUG: Cart before removing: {cart}")

    if str(product_id) in cart:
        # اینجا باید بررسی کنی که آیا تعداد محصول بیشتر از 1 است یا نه.
        # اگر فقط یک عدد بود، کلا حذفش کن. اگر نه، تعداد رو کم کن.
        # در حال حاضر، اگر محصول رو پیدا کنه، کلاً حذفش می‌کنه.
        # اگر میخواهی فقط یک عدد ازش کم کنی:
        # if cart[str(product_id)] > 1:
        #     cart[str(product_id)] -= 1
        # else:
        #     del cart[str(product_id)]
        
        # کد فعلی شما که کلا محصول رو حذف می‌کنه:
        del cart[str(product_id)]

    request.session['cart'] = cart
    # مهم: این خط زیر رو اضافه کن تا مطمئن بشیم سشن ذخیره میشه
    request.session.modified = True 
    print(f"DEBUG: Cart after removing and saving to session: {request.session.get('cart')}")
    print(f"DEBUG: Redirecting to cart:cart_detail after removing product {product_id}")
    return redirect('cart:cart_detail') # <-- اصلاح شده اینجا

def cart_detail(request): # نام این تابع رو از shapping_cart به cart_detail تغییر دادم تا با URL همخوانی داشته باشه
    print("DEBUG: cart_detail view called.")
    cart = request.session.get('cart', {})
    print(f"DEBUG: Cart content in cart_detail: {cart}") # اینجا وضعیت سشن رو چک می‌کنیم

    cart_items = []
    total_price = 0

    # برای هر محصول در سبد خرید
    for product_id, quantity in cart.items():
        try:
            # اطلاعات کامل محصول رو از دیتابیس می‌گیریم
            product = get_object_or_404(Product, id=product_id)
            # مطمئن شو که quantity یک عدد است. در صورت نیاز به int تبدیل کن
            quantity_int = int(quantity) 
            item_total = product.price * quantity_int # قیمت کل این آیتم

            cart_items.append({
                'product': product,
                'quantity': quantity_int,
                'total': item_total,
            })

            total_price += item_total # جمع کل قیمت‌ها
            print(f"DEBUG: Added product {product.title} (ID: {product_id}) with quantity {quantity_int} to cart_items.")
        except Exception as e:
            print(f"ERROR: Could not find product with ID {product_id} in database. Error: {e}")
            # اگر محصولی پیدا نشد، اون رو از سشن حذف می‌کنیم تا خطای بعدی نده
            if str(product_id) in request.session['cart']:
                del request.session['cart'][str(product_id)]
                request.session.modified = True
                print(f"DEBUG: Removed invalid product ID {product_id} from session.")

    # اطلاعات رو به قالب cart.html می‌فرسته
    print(f"DEBUG: Final cart_items count: {len(cart_items)}")
    print(f"DEBUG: Final total_price: {total_price}")
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def checkout(request):
    print("DEBUG: checkout view called.")
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items(): # تغییر از item_data به quantity مستقیم
        try:
            product = get_object_or_404(Product, id=int(product_id))
            quantity_int = int(quantity) # مطمئن شو که quantity یک عدد است.
            item_total = product.price * quantity_int
            total_price += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity_int,
                'total': item_total,
            })
            print(f"DEBUG: Added product {product.title} to checkout items.")
        except Exception as e:
            print(f"ERROR: Could not find product with ID {product_id} for checkout. Error: {e}")
            # نیازی به حذف از سشن اینجا نیست، چون فقط برای نمایش است.

    print(f"DEBUG: Final checkout cart_items count: {len(cart_items)}")
    print(f"DEBUG: Final checkout total_price: {total_price}")
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
