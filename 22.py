import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🍔 Simulasi Model Antrian M/M/1 - Fast Food Restaurant")

st.sidebar.subheader("📌 Petunjuk Input")
st.sidebar.markdown(
    "- λ: Rata-rata pelanggan datang per jam\n"
    "- μ: Rata-rata pelanggan dilayani per jam\n"
    "Contoh: 15 pelanggan/jam datang, pelayanan 3 menit → μ = 20"
)

# Input dari user
lambda_rate = st.number_input("Rata-rata Kedatangan Pelanggan (λ) per jam", value=15.0, min_value=0.1)
mu_rate = st.number_input("Rata-rata Pelayanan (μ) per jam", value=20.0, min_value=0.1)

if lambda_rate >= mu_rate:
    st.error("⚠ Sistem overload! λ harus lebih kecil dari μ untuk M/M/1.")
else:
    # Perhitungan model M/M/1
    rho = lambda_rate / mu_rate                      # Utilisasi
    W = 1 / (mu_rate - lambda_rate)                  # Waktu dalam sistem
    Wq = W - (1 / mu_rate)                           # Waktu tunggu
    L = lambda_rate * W                              # Rata-rata pelanggan dalam sistem
    Lq = lambda_rate * Wq                            # Rata-rata dalam antrian

    # Hasil Perhitungan
    st.subheader("📊 Hasil Perhitungan Model M/M/1")
    st.write(f"*Utilisasi Kasir (ρ):* {rho:.2%}")
    st.write(f"*Waktu Rata-rata dalam Sistem (W):* {W*60:.2f} menit")
    st.write(f"*Waktu Rata-rata dalam Antrian (Wq):* {Wq*60:.2f} menit")
    st.write(f"*Jumlah Rata-rata Pelanggan dalam Sistem (L):* {L:.2f} orang")
    st.write(f"*Jumlah Rata-rata Pelanggan dalam Antrian (Lq):* {Lq:.2f} orang")

    # Visualisasi: jumlah rata-rata pelanggan dalam antrian (Lq) terhadap λ
    st.subheader("📈 Grafik: Jumlah Antrian vs Kedatangan")
    lambda_vals = np.linspace(1, mu_rate - 0.1, 100)
    Lq_vals = (lambda_vals**2) / (mu_rate * (mu_rate - lambda_vals))

    fig, ax = plt.subplots()
    ax.plot(lambda_vals, Lq_vals, color='blue')
    ax.axvline(lambda_rate, color='red', linestyle='--', label='λ Saat Ini')
    ax.set_xlabel("Rata-rata Kedatangan (λ)")
    ax.set_ylabel("Jumlah Rata-rata Antrian (Lq)")
    ax.set_title("Jumlah Antrian vs Tingkat Kedatangan")
    ax.legend()
    st.pyplot(fig)

    st.success("✅ Simulasi berhasil dihitung.")
