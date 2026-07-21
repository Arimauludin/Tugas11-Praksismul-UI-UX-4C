from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'arima_crunch_secret_key'

# Data Produk Makroni
PRODUCTS = [
    {
        'id': 1,
        'name': 'Makroni Api Level 1 (Daun Jeruk)',
        'price': 12000,
        'desc': 'Pedas gurih nagih dengan aroma daun jeruk segar.',
        'image': 'makroni-level1.jpeg'
    },
    {
        'id': 2,
        'name': 'Makroni Neraka Level 3 (Extra Pedas)',
        'price': 15000,
        'desc': 'Pedas nampol khusus kamu yang ngaku jago pedas!',
        'image': 'makroni-level2.jpeg'
    },
    {
        'id': 3,
        'name': 'Makroni LaVa Cheese (Spicy Cheese)',
        'price': 18000,
        'desc': 'Perpaduan keju lumer dan bubuk cabai super pedas.',
        'image': 'makroni-level3.jpeg'
    }
]

# Database Dummy untuk menyimpan Riwayat Pesanan
ORDER_HISTORY = [
    {
        'id': 'INV-1001',
        'nama': 'Budi Santoso',
        'produk': 'Makroni Neraka Level 3 (Extra Pedas)',
        'jumlah': 2,
        'total': 30000,
        'estimasi': '2-3 Hari Kerja',
        'status': 'Dikirim',
        'can_return': True
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS[:3])

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    success_order = None
    if request.method == 'POST':
        nama = request.form.get('nama')
        telepon = request.form.get('telepon')
        alamat = request.form.get('alamat')
        produk_id = int(request.form.get('produk_id'))
        jumlah = int(request.form.get('jumlah'))

        # Cari data produk
        selected_product = next((p for p in PRODUCTS if p['id'] == produk_id), None)
        
        if selected_product:
            total_harga = selected_product['price'] * jumlah
            order_id = f"INV-{1001 + len(ORDER_HISTORY)}"
            
            # Buat objek pesanan baru
            new_order = {
                'id': order_id,
                'nama': nama,
                'produk': selected_product['name'],
                'jumlah': jumlah,
                'total': total_harga,
                'estimasi': '2-3 Hari Kerja',
                'status': 'Diproses',
                'can_return': True
            }
            
            # Simpan ke riwayat
            ORDER_HISTORY.append(new_order)
            success_order = new_order

    return render_template('checkout.html', products=PRODUCTS, success_order=success_order)

@app.route('/history')
def history():
    return render_template('history.html', orders=ORDER_HISTORY)

@app.route('/return/<order_id>', methods=['POST'])
def return_order(order_id):
    # Cari pesanan dan ubah statusnya menjadi Return
    for order in ORDER_HISTORY:
        if order['id'] == order_id:
            order['status'] = 'Pengajuan Return Diproses'
            order['can_return'] = False
            flash(f'Pengajuan return untuk pesanan {order_id} berhasil dikirim!', 'warning')
            break
    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)