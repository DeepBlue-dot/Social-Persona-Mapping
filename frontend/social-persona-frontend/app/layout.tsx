import "./globals.css";
import { Inter } from "next/font/google";
const inter = Inter({ subsets: ["latin"] });


export const metadata = {
title: "Social Persona Mapping Dashboard",
description: "Analyze and visualize online personas",
};


import { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
return (
<html lang="en">
<body className={`${inter.className} bg-black text-white`}>{children}</body>
</html>
);
}