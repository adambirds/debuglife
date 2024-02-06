import Navbar from '@/components/common/frontend/NavBar'
import FooterComponent from "@/components/common/frontend/footer/Footer";
import { footerNavigation, footerSocial } from "@/fixtures/footerData";

const navigation = [
    {title: "Home", href: "/", current: false},
    {title: "Features", href: "/features", current: false},
    {title: "Pricing", href: "/pricing", current: false},
    {title: "About", href: "/about", current: false},
    {title: "FAQs", href: "/faqs", current: true},
    {title: "Blog", href: "/blog", current: false},
    {title: "Contact", href: "/contact", current: false},
]

export default function FAQsPage() {
    return (
        <div>
            <Navbar
                navigation={navigation}
            />

            <FooterComponent navigation={footerNavigation} social={footerSocial} />
        </div>
    )
}
