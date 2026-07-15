import "./globals.css";
export const metadata = { title: "Tolveris Launchpad", description: "Safe digital banking with confidence" };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
